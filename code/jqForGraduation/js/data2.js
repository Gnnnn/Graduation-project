$(function() {
    var pivotGrid = $("#pivotgrid").dxPivotGrid({
        allowSortingBySummary: true,
        allowFiltering: true,
        showBorders: true,
        showColumnGrandTotals: false,
        showRowGrandTotals: false,
        showRowTotals: false,
        showColumnTotals: false,
        fieldChooser: {
			enabled: true,
			height: 400
        },
        dataSource: {
            fields: [{
                caption: "manufacturer",
                width: 120,
                dataField: "manufacturer",
                area: "column",
                sortBySummaryField: "Total"
            }, {
                caption: "id",
                dataField: "id",
                dataType: "number",
                width: 130,
                area: "row"
            }, {
                caption: "Total",
                dataField: "sampleId",
                dataType: "number",
                summaryType: "sum",
                area: "data"
            }],
            store: sales
        }
    }).dxPivotGrid("instance");

});