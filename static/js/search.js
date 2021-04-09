const input = document.getElementById("searchBox");
const searchResults = document.getElementById("searchResults");

function renderAutocompleteList(results) {
    searchResults.innerHTML = "";

    for (let result of results) {
        const item = document.createElement("a")
        item.classList.add("list-group-item", "list-group-item-action");
        item.innerText = result["name"];
        searchResults.appendChild(item);
    }
}

input.addEventListener('input', (e) => {
    let userText = e.target.value;

    if (userText) {
        fetch(`http://127.0.0.1:5000/search?query=${encodeURIComponent(userText)}`)
            .then((res) => res.json())
            .then(renderAutocompleteList);
    } else {
        emptySearchDiv();
    }
});

function emptySearchDiv() {
    searchResults.innerHTML = "";
}