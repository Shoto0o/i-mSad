// Function to update the temperature slider and display the value
function updateTemperature() {
    const slider = document.getElementById("temperature-slider");
    const temperature = slider.value;
    document.getElementById("temperature-value").textContent = temperature;
}

// Function to request the weather information
async function requestWeather() {
    const location = prompt("Please enter your location:");

    if (!location) return;

    const apiKey = "54accd9e4a3a33fadab4b8114f4afd37";  // Replace with your OpenWeatherMap API key
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${location}&units=metric&appid=${apiKey}`;

    const response = await fetch(apiUrl);
    const data = await response.json();

    const weatherCondition = data.weather[0].main;
    const temperature = data.main.temp;
    const humidity = data.main.humidity;
    const weatherIcon = weatherCondition === 'Clear' ? '☀️' : weatherCondition === 'Rain' ? '🌧️' : '🌥️';

    // Update the weather widget with the current weather info
    document.getElementById("weather-info").innerHTML = `
        <p>${weatherCondition} ${weatherIcon}</p>
        <p>Temperature: ${temperature}°C</p>
        <p>Humidity: ${humidity}%</p>
    `;
}

// Function to fetch performance suggestions
async function getPerformanceSuggestion() {
    const response = await fetch('/performance_suggestions', { method: 'POST' });
    const data = await response.json();
    document.getElementById("suggestion-text").textContent = data.suggestion;
}
