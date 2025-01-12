# Web Spreadsheet Application

A Google Sheets-like web application built with vanilla JavaScript for the frontend and Django for the backend.

## Technical Stack & Architecture

### Frontend
- *Vanilla JavaScript*: Chosen for its lightweight nature and to demonstrate core programming concepts without framework abstractions
- *CSS Grid*: Used for the spreadsheet layout, providing excellent performance for large grids
- *HTML5*: Utilizing modern features like contentEditable for cell editing

### Backend
- *Django*: Chosen for its robust ORM, built-in authentication, and excellent security features
- *MySQL*: (Recommended database) for reliable data storage and JSON field support

### Data Structures

#### Frontend
1. *Grid Management*
   - Using DOM elements in a CSS Grid layout
   - Each cell is a div with dataset attributes for row and column positions
   - Cell data stored in a JavaScript object with key format "column,row"

2. *Formula Evaluation*
   - Recursive descent parser for formula evaluation
   - Support for cell references and ranges
   - Caching of intermediate results for performance

#### Backend
1. *Database Schema*
   - Spreadsheet model for document management
   - Cell model for individual cell data
   - JSON field for storing cell styling information

2. *Data Transfer*
   - REST API endpoints for saving and loading spreadsheets
   - Bulk operations for efficient database interactions

### Key Features Implementation

1. *Cell Dependencies*
   - Dependency graph maintained for formula calculations
   - Efficient updates using topological sorting
   - Circular reference detection

2. *Formatting*
   - Style information stored in cell's style attribute
   - Persistent storage in database JSON field