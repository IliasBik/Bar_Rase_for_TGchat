# Bar_Rase_for_TGchat
You can make a video where the chart that displays the number of messages changes over time.

This project visualizes user activity in a Telegram chat over time using an animated bar chart race. It processes exported Telegram chat data (result.json) and displays how many messages each user has sent per day, with smooth animation.

Features:
  Reads Telegram's exported result.json (from Export chat history function) and extracts message counts by users per day.
  Bar Chart Race Generation
    Uses bar_chart_race and matplotlib to animate message counts over time:
    Horizontal animation
    Sorted bars (top N users)
    Smooth transitions (interpolate_period=True)
    Labels and title included
    Customizable color map and layout    
  Output Options:
    Generates output as an animated .gif (optionally .mp4), suitable for social media or presentations.

Input Format:
To use this tool, export your Telegram chat history (as JSON) and place the result.json file in the project directory.

Structure:

{
  "name": "...",
  "messages": [
    {
      "type": "message",
      "date": "2024-01-01T10:00:00",
      "from": "User Name",
      "text": ...
    },
    ...
  ]
}
How it Works
  Parses messages: Extracts sender and date from every message.
  Aggregates daily totals: Counts cumulative messages for each user by day.
  Creates DataFrame: Builds a pandas DataFrame where rows are time steps and columns are users.
  Animates chart: Generates animated bar chart of message counts using bar_chart_race.
