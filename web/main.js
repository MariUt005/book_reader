async function display_books() {
    let path = await eel.get_path()();
    let books = await eel.get_txt(path)();
    let result = "";
    for (let book in books) {
        result += "<p>" + books[book] + "</p>";
    }
    document.getElementById("content").innerHTML = result;
}

display_books();