document.addEventListener("DOMContentLoaded", function () {
  const moodData = window.moodData || {};
  const heatmap = document.getElementById("heatmap");

  const moodColors = {
    'Happy': '#28a745', 'Sad': '#6c757d', 'Angry': '#dc3545', 'Anxious': '#fd7e14',
    'Neutral': '#17a2b8', 'Excited': '#ffc107', 'Depressed': '#343a40',
    'Stressed': '#e83e8c', 'Calm': '#20c997', 'Lonely': '#6f42c1',
    'Frustrated': '#ff4c4c', 'Bored': '#adb5bd', 'Hopeful': '#00bcd4',
    'Grateful': '#9ccc65'
  };

  const today = new Date();
  const start = new Date();
  start.setDate(today.getDate() - 6 * 7); 

  const date = new Date(start);
  const weeks = [];

  while (date <= today) {
    const dayOfWeek = date.getDay();
    if (dayOfWeek === 0 || weeks.length === 0) {
      weeks.push([]);
    }

    const dateStr = date.toISOString().split("T")[0];
    const mood = moodData[dateStr];
    const color = moodColors[mood] || '#eaeaea';

    weeks[weeks.length - 1].push({ dateStr, color, mood });
    date.setDate(date.getDate() + 1);
  }

  weeks.forEach(week => {
    const weekCol = document.createElement("div");
    weekCol.className = "week-column";

    for (let i = 0; i < 7; i++) {
      const day = week[i];
      const dayDiv = document.createElement("div");
      dayDiv.className = "day-cell";

      if (day) {
        dayDiv.style.backgroundColor = day.color;
        dayDiv.title = `${day.dateStr} - ${day.mood || 'No mood logged'}`;
      }

      weekCol.appendChild(dayDiv);
    }

    heatmap.appendChild(weekCol);
  });
});