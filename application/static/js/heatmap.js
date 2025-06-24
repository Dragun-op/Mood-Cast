document.addEventListener("DOMContentLoaded", function () {
  const chartDom = document.getElementById("heatmap");
  const myChart = echarts.init(chartDom);

  const moodData = window.moodData;
  const moodColors = window.moodColors;

  const seriesData = Object.entries(moodData).map(([date, mood]) => ({
    name: date,
    value: [date, 1],
    itemStyle: {
      color: moodColors[mood] || '#dcdcdc',
    },
  }));

  const option = {
    tooltip: {
      position: 'top',
      formatter: function (params) {
        const date = params.name;
        const mood = moodData[date];
        return `${date}: ${mood || "No mood"}`;
      }
    },
    calendar: {
      range: [new Date().getFullYear()],
      cellSize: ['auto', 30], // ← increase this!
      itemStyle: {
        borderWidth: 0.5,
        borderColor: '#999',
      },
      yearLabel: { show: false },
      dayLabel: { nameMap: 'en', fontSize: 12 },
      monthLabel: { nameMap: 'en', fontSize: 14 }
    },
    series: [{
      type: 'heatmap',
      coordinateSystem: 'calendar',
      data: seriesData
    }]
  };

  myChart.setOption(option);
});