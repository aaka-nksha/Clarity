# Clarity: The Next Action Engine

"Stuck, not lazy." This tool helps you break through the friction of indecision by providing the single most effective next step based on your goals and available time.

## Tech Stack
- **Backend**: Python (Flask)
- **Frontend**: HTML5, Modern CSS (Glassmorphism), Lucide Icons
- **Data Architecture**:
    - **Kafka Integration**: Ready for event-stream processing of productivity markers.
    - **PySpark Integration**: Ready for big-data analytics on goal completion trends.

## How to Run
1. Ensure your Python environment is active.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the server:
   ```bash
   python app.py
   ```
4. Open your browser at `http://localhost:5000`

## Features
- **Premium Design**: Dark mode aesthetic with glassmorphism and fluid transitions.
- **Dynamic Action Logic**: Cross-references goals with available time to pick the best action.
- **Micro-Slicing**: Automatically breaks down large goals if time is short.
