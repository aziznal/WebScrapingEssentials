

const get_page_y = () => {
    /// This returns distance scrolled from the top of the page

    let page_y = window.pageYOffset;

    return page_y;

}

const display_page_y = (element_id) => {

    let page_y = get_page_y();

    let element = document.getElementById(element_id);

    element.innerHTML = "Page Y = " + "<strong>" + page_y + "<strong>";

}

// Y Page Offset Counter
(() => {
    setInterval(() => display_page_y('page_offset_display'), 10);
})();

const get_element_y = (element_id, display_to) => {
    
    const element = document.getElementById(element_id);
    let element_rect = element.getBoundingClientRect();
    element_y = parseInt(element_rect.top + window.scrollY);

    display_element = document.getElementById(display_to);
    display_element.innerHTML = "Element Y: " + element_y;

    return element_y;
}

(() => {
    setInterval(() => get_element_y('smooth-vertical', 'smooth-vertical-current-y'), 1);
    setInterval(() => get_element_y('instant-vertical', 'instant-vertical-current-y'), 1);
})();
