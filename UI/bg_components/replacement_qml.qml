
ApplicationWindow {
    visible: true

    width: 48
    height: 48

    Component.onCompleted: {

        var len = contentItem.children.length
        var long_width = 0
        var long_height = 0
        for(var x=0; x<len; x++) {
            var curr_width = contentItem.children[x].width
            var curr_height = contentItem.children[x].height

            if(curr_width > long_width) {
                long_width = curr_width
            }
            if(curr_height > long_height) {
                if(curr_height > 512) {
                    long_height = 512
                } else {
                    long_height = curr_height
                }
            }
        }

        var st1 = this.screen.width - long_width
        var st2 = this.screen.height - long_height

        this.setX(st1/2)
        this.setY(st2/2)

        width = long_width
        height = long_height
    }
