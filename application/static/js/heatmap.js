document.addEventListener("DOMContentLoaded", function () {
  const calendar = document.getElementById("calendar");
  const moodData = window.moodData || {};

  if (!calendar) return;

  const today = new Date();
  const start = new Date(today.getFullYear(), today.getMonth() - 5, 1); // show 6 months
  const end = today;

  const dateIterator = new Date(start);
  const moodColors = {
    'Happy': '#28a745',
    'Sad': '#6c757d',
    'Angry': '#dc3545',
    'Anxious': '#fd7e14',
    'Neutral': '#17a2b8',
    'Excited': '#ffc107',
    'Depressed': '#343a40',
    'Stressed': '#e83e8c',
    'Calm': '#20c997',
    'Lonely': '#6f42c1',
    'Frustrated': '#ff4c4c',
    'Bored': '#adb5bd',
    'Hopeful': '#00bcd4',
    'Grateful': '#9ccc65'
  };

  while (dateIterator <= end) {
    const dateStr = dateIterator.toISOString().split('T')[0];
    const mood = moodData[dateStr];
    const color = moodColors[mood] || '#f0f0f0';

    const cell = document.createElement("div");
    cell.classList.add("calendar-cell");
    cell.style.backgroundColor = color;
    cell.title = `${dateStr}${mood ? ' - ' + mood : ''}`;
    calendar.appendChild(cell);

    dateIterator.setDate(dateIterator.getDate() + 1);
  }
});