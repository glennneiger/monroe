function loadingDialog(href) {
        var $dialog = $('<div></div>')
        .html('Loading.')
        .dialog({
                autoOpen: true,
                title: 'Monroe County Foreclosures',
                modal: true,
        });
        window.location.href=href
}

