const fetch = require("node-fetch");
const baseUrl = "http://127.0.0.1:8000/api/v1/shehab/search";
const q = typeof query !== "undefined" ? query : "";
const packages = typeof find_packages !== "undefined" ? find_packages : false;
const url = `${baseUrl}?query=${encodeURIComponent(q)}&find_packages=${packages}`;
try {
    const response = await fetch(url, { method: "GET", headers: { "Accept": "application/json" } });
    const data = await response.json();
    return JSON.stringify({ success: true, items: data || [] });
} catch (error) {
    return JSON.stringify({ success: false, error: error.message, items: [] });
}