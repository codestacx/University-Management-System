function makeChallanPDF(name, canvasID) {
    var url = `http://localhost:8000/get-challan-pdf/${name}`;

    // Loaded via <script> tag, create shortcut to access PDF.js exports.
    var pdfjsLib = window['pdfjs-dist/build/pdf'];

    // The workerSrc property shall be specified.
    pdfjsLib.GlobalWorkerOptions.workerSrc = 'static/js/pdf.worker.js';

    // Asynchronous download of PDF
    var loadingTask = pdfjsLib.getDocument(url);
    loadingTask.promise.then(function (pdf) {
        console.log('PDF loaded');

        // Fetch the first page
        var pageNumber = 1;
        pdf.getPage(pageNumber).then(function (page) {
            console.log('PDF.js: Page loaded');

            // Prepare canvas using PDF page dimensions
            var canvas = document.getElementById(canvasID);
            var context = canvas.getContext('2d');

            var scale = canvas.width / page.getViewport({ scale: 1.0 }).width;
            var viewport = page.getViewport({ scale: scale * 2 });

            canvas.height = viewport.height;
            canvas.width = viewport.width;

            // Render PDF page into canvas context
            var renderContext = {
                canvasContext: context,
                viewport: viewport
            };
            var renderTask = page.render(renderContext);
            renderTask.promise.then(function () {
                console.log('PDF.js: Page rendered');
            });
        });
    }, function (reason) {
        // PDF loading error
        console.error(reason);
    });
}

function filter(inputSelector = '#filter', tableRowSelector = '.to-filter-row', comparator) {
    const toFilterRows = $(tableRowSelector)

    $(inputSelector).on('input change', function (e) {
        const filterVal = e.target.value

        toFilterRows.removeClass('hidden')

        if (filterVal === '') {
            return
        }

        const filtered = toFilterRows.toArray().filter((row, index) => {
            return comparator($(row), filterVal)
        })

        filtered.forEach(function (row, index) {
            $(row).addClass('hidden')
        })
    })
}