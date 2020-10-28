
const getPageY = () => {
    /// This returns distance scrolled from the top of the page

    let page_y = window.pageYOffset;

    return page_y;

}

const displayPageY = (element_id) => {

    let page_y = getPageY();

    let element = document.getElementById(element_id);

    element.innerHTML = "Page Y = " + "<strong>" + page_y + "<strong>";

}

// ### Y Page Offset Counter
(() => {
    setInterval(() => displayPageY('page_offset_display'), 10);
})();

const getElementY = (element_id, display_to) => {
    
    const element = document.getElementById(element_id);
    // let element_rect = element.getBoundingClientRect();
    // element_y = parseInt(element_rect.top + window.scrollY);

    element_y = element.offsetTop

    display_element = document.getElementById(display_to);
    display_element.innerHTML = element_y;

    return element_y;
}

// ### Scroll tests - y offset displays
(() => {
    setInterval(() => getElementY('smooth-vertical', 'smooth-vertical-current-y'), 1);
    setInterval(() => getElementY('instant-vertical', 'instant-vertical-current-y'), 1);
})();


const showOnHeightReached = (element_id, height) => {
    /// Hide given element until the given height is reached (by scrolling to it)
    element = document.getElementById(element_id);
    element.style.visibility = "hidden";

    // Check for correct height every ten seconds
    let timer = setInterval(() => {
        let height_passed = getPageY() >= height;

        if (height_passed){
            element.style.visibility = "visible";
            element.innerHTML = "visible"
            clearInterval(timer);
        }

    }, 10);
}

// ### Set to show element after certain height is passed
(() => {
    setTimeout(() => showOnHeightReached('hidden-element', 2000), 1);
})();


const showSlowInputResult = () => {
    let input_field = document.getElementById("slow-input-field");
    let result_output = document.getElementById("slow-input-results")

    inputted_text = input_field.value
    console.log(inputted_text);
    result_output.innerHTML = inputted_text

}

const passTest = (parent_element) => {

    // console.log(parent_element.style.opacity);
    // parent_element.style.opacity = '100%';

    parent_element.children[0].style.opacity = 1;

}

const testButtonOutput = () => {

    const output_element = document.getElementById("button-onclick-output")

    output_element.innerHTML = "Button has been clicked!"
    
}
