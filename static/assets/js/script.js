$(document).ready(function(){
    var table = $('#example').DataTable({
       buttons:['copy', 'csv', 'excel','pdf','print']
    });

    table.buttons().container().appendTo('#example_wrapper .col-md-6:eq(0)');
})


if ( ! $.fn.DataTable.isDataTable( '#example' ) ) {
  $('#example').DataTable();
}

$('#example').DataTable().destroy();
$('#example').DataTable();

