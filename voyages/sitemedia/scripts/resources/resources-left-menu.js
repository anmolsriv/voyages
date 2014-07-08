$(document).ready(function() {
    /* Collapsible boxes */
    $("div .box-button, div .box-button-collapsed").click(function(ev){
	    var curBox = $(this).parent().parent().parent().parent().parent().parent().parent();
        var children = curBox.children();
        if ($(this).hasClass("box-button")){
            expandRow(curBox, $(this))
            $(this).toggleClass("box-button box-button-collapsed");
        } else{
            collapseRow(curBox, $(this))
            $(this).toggleClass("box-button-collapsed box-button");
        }
    })

    $("div.lookup-checkbox-list-item-collapsed").click(function(ev){
        var a = 4;
        var b = $(this).parent().children();
    })
});

function collapseRow(table, button){
    table.children().each(function( index ){
        if ($(this).hasClass("row-collapsed")){
            $(this).toggleClass("row-collapsed row");
        }
    });
    var a = $(button).parent().parent().parent().parent().parent().parent().children();
    if (a.hasClass("box-set-upper-row-bottom-left-collapsed")){
        a.first().removeClass('box-set-upper-row-bottom-left-collapsed').addClass('box-set-upper-row-bottom-left')
        a.eq(1).removeClass('box-set-upper-row-bottom-middle-collapsed').addClass('box-set-upper-row-bottom-middle')
        a.eq(2).removeClass('box-set-upper-row-bottom-right-collapsed').addClass('box-set-upper-row-bottom-right')
    }
    if (a.hasClass("box-upper-row-left-collapsed")){
        a.first().removeClass('box-upper-row-left-collapsed').addClass('box-upper-row-left')
        a.eq(1).removeClass('box-upper-row-middle-collapsed').addClass('box-upper-row-middle')
        a.eq(2).removeClass('box-upper-row-right-collapsed').addClass('box-upper-row-right')
    }

}

function expandRow(table, button){
    table.children().each(function( index ){
        if ($(this).hasClass("row")){
            $(this).toggleClass("row row-collapsed");
        }
    });
    var a = $(button).parent().parent().parent().parent().parent().parent().children();
    if (a.hasClass("box-set-upper-row-bottom-left")){
        a.first().removeClass('box-set-upper-row-bottom-left').addClass('box-set-upper-row-bottom-left-collapsed')
        a.eq(1).removeClass('box-set-upper-row-bottom-middle').addClass('box-set-upper-row-bottom-middle-collapsed')
        a.eq(2).removeClass('box-set-upper-row-bottom-right').addClass('box-set-upper-row-bottom-right-collapsed')
    }
    if (a.hasClass("box-upper-row-left")){
        a.first().removeClass('box-upper-row-left').addClass('box-upper-row-left-collapsed')
        a.eq(1).removeClass('box-upper-row-middle').addClass('box-upper-row-middle-collapsed')
        a.eq(2).removeClass('box-upper-row-right').addClass('box-upper-row-right-collapsed')
    }
}

function filter_edit_list() {
    var text_to_search = $("#query-text-origin").val()
    var items = $('#origin_list').children()

    if (text_to_search == "") {
        items.each(function( index ) {
           $(this).removeClass("hidden");
        });
    } else {
        items.each(function( index ) {
            if ($(this).children().eq(2).text().toLowerCase().indexOf(text_to_search) >= 0) {
                $(this).removeClass("hidden");
            } else {
                $(this).addClass("hidden");
            }
        });
    }
}

function expandable_embarkation(div, id){
    $(div).toggleClass("lookup-checkbox-list-item-collapsed lookup-checkbox-list-item-expanded");
    var a = $(div).parent().parent().parent().find("#tr" + id + "_child");
    if (a.css('display') == 'none'){
        a.removeAttr('style');
    } else{
        a.css({ 'display': "none" });
    }


    return false;
}