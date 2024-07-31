function movetab(link) {
    var url = new URL(link)
    window.open(url, "_blank")

}

$(document).ready(function () {
    $('#editModal').on('show.bs.modal', function(event) {
        let editform = document.forms['editform'];
        let button = $(event.relatedTarget);
        let name = button.data('name');
        let writer = button.data('writer');
        let content = button.data('content');
        let img = button.data('img');
        let cost = button.data('cost');
        cost = parseFloat(cost,10);
        let id = button.data('id');
        console.log(id)
        //pass data
        $('#editname').val(name);
        $('#editwriter').val(writer);
        $('#editcontent').val(content);
        $('#editimg').val(img);
        $('#editcost').val(cost);
        editform.action = `/manager/edit/product/${id}`;

    }); 

    $('#deleteModal').on('show.bs.modal', function(event) {
        let delform = document.forms['delform'];
        let button = $(event.relatedTarget);
        let name = button.data('name'); 
        let id = button.data('id');
        console.log(id)
        $('#delname').val(name);
        delform.action = `/manager/delete/product/${id}`;
    });
})



