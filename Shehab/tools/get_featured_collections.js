const fetch = require("node-fetch");
const collectionType = typeof type !== "undefined" ? type : "newest";
const url = `http://127.0.0.1:8000/api/v1/shehab/collections/${collectionType}`;
try {
    const response = await fetch(url, { method: "GET", headers: { "Accept": "application/json" } });
    const data = await response.json();
    return JSON.stringify({ success: true, items: data || [] });
} catch (error) {
    return JSON.stringify({ success: false, error: error.message, items: [] });
}