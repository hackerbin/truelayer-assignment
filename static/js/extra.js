$(document).ready(function () {
    $('#dataTable').DataTable();
});


function generateTable(item) {
    var _table = '<table class="table table-bordered">';
    Object.keys(item).forEach(function (_key) {
        _table = _table + '<tr><td><strong>' + _key + '</strong></td><td>' + JSON.stringify(item[_key]) + '</td></tr>'
    });
    _table = _table + '</table>';
    return _table
}

function showDetails(item_obj) {
    var item = JSON.parse(JSON.stringify(item_obj));
    Swal.fire({
        title: 'Account Details',
        width: 800,
        html: generateTable(item),
        showCloseButton: true,
    })
}