async function fetchNews() {
    try {
        const response = await fetch('/fetch_news');
        const news = await response.json();

        const newsContainer = document.getElementById('news-container'); // Updated ID to match HTML
        newsContainer.innerHTML = ""; // Clear previous news

        news.forEach(article => {
            const card = `
                <div class="news-card">
                    <h3>${article.title}</h3>
                    <p>${article.source}</p>
                    <p>${article.description}</p>
                    <a href="${article.url}" target="_blank">Read More</a>
                </div>
            `;
            newsContainer.innerHTML += card;
        });
    } catch (error) {
        console.error("Error fetching news:", error);
    }
}

document.addEventListener('DOMContentLoaded', fetchNews);
