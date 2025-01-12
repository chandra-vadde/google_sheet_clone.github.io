# views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Spreadsheet, Cell
import json

def index(request):
    return render(request, 'spreadsheet/index.html')

@csrf_exempt
def save_spreadsheet(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        spreadsheet = Spreadsheet.objects.create(
            name=data.get('name', 'Untitled'),
            user=request.user
        )
        
        cells_data = data.get('cells', {})
        bulk_cells = []
        
        for cell_key, cell_data in cells_data.items():
            col, row = map(int, cell_key.split(','))
            bulk_cells.append(Cell(
                spreadsheet=spreadsheet,
                row=row,
                column=col,
                value=cell_data.get('value'),
                formula=cell_data.get('formula'),
                style=cell_data.get('style', {})
            ))
        
        Cell.objects.bulk_create(bulk_cells)
        return JsonResponse({'id': spreadsheet.id})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def load_spreadsheet(request, spreadsheet_id):
    try:
        spreadsheet = Spreadsheet.objects.get(id=spreadsheet_id, user=request.user)
        cells = Cell.objects.filter(spreadsheet=spreadsheet)
        
        data = {
            'name': spreadsheet.name,
            'cells': {
                f"{cell.column},{cell.row}": {
                    'value': cell.value,
                    'formula': cell.formula,
                    'style': cell.style
                }
                for cell in cells
            }
        }
        return JsonResponse(data)
    except Spreadsheet.DoesNotExist:
        return JsonResponse({'error': 'Spreadsheet not found'}, status=404)