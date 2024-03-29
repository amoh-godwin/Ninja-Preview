import QtQuick
import QtQuick.Controls.Basic
import QtQuick.Layouts
import QtQuick.Dialogs
//import QtGraphicalEffects 1.0
import "others" as Other
import "Components" as Comp

ApplicationWindow {
    id: mainWindow

    property int prevX
    property int prevY
    property int current_index
    property string qt_version: ''

    property QtObject preview

    width: 972
    height: 600
    visible: true
    title: "Empty"
    color: "transparent"

    flags: Qt.Window | Qt.FramelessWindowHint

    FontLoader { id: __main__font__; source: "fonts/materialdesignicons/materialdesignicons-webfont.ttf"}
    FontLoader { id: __fa__font__; source: "fonts/fa_solid.otf"}

    signal bootUp(string status)
    signal addfiles(string ctnt)
    signal removeFromView(int index)
    signal runFile(string filename)
    signal runInPhoneFrame(string filename)
    signal runInHotReloadMode(string filename, int current_index)

    //Component.onCompleted: bootUp('Loaded');

    onBootUp: {
        preview.bootUp(status)
    }

    onAddfiles: {

        var filelist = ctnt.split(',')
        var len = filelist.length

        while (len > 0) {
            var url = filelist[len - 1]
            var name = url.substring(8, url.length)
            view.model.append({"url": url, "name": name})
            len--
            view.currentIndex = view.count - 1
        }

    }

    onRemoveFromView: {
        view.model.remove(index)
    }

    onRunFile: {
        // call the python code to run the filename
        title = filename
        infoView.model.append({"content":""})
        current_index = infoView.model.count - 1
        preview.run(filename, current_index)
    }

    onRunInPhoneFrame: {
        title = filename
        infoView.model.append({"content":""})
        current_index = infoView.model.count - 1
        preview.run_in_phone_frame(filename, current_index)
    }

    onRunInHotReloadMode: {
        title = filename
        infoView.model.append({"content":""})
        var view_index = infoView.model.count - 1
        preview.run_in_hot_reload_mode(filename, view_index, current_index)
    }


    header: Rectangle {
        anchors.left: parent.left
        anchors.leftMargin: 6
        width: bg.width
        height: 42
        color: "transparent"

        Rectangle {
            anchors.top: parent.top
            anchors.topMargin: 6
            width: parent.width
            height: parent.height - 6
            color: "#191b1f"

            RowLayout {
                anchors.fill: parent

                Rectangle {
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    color: "transparent"

                    RowLayout {

                        height: parent.height

                        Image {
                            Layout.leftMargin: 15
                            Layout.alignment: Layout.Center
                            sourceSize.width: 18
                            sourceSize.height: 18
                            source: "icons/logo.png"
                        }

                        Text {
                            Layout.leftMargin: 15
                            width: 200
                            font {
                                family: "Segoe UI Semilight"
                                pixelSize: 12
                            }
                            elide: Text.ElideMiddle
                            text: title + "  - "
                            color: "white"
                        }

                        Text {
                            font {
                                family: "Segoe UI Semilight"
                                pixelSize: 12
                            }
                            text: "Ninja-Preview (" + qt_version + ")"
                            color: "white"
                        }


                    }

                    MouseArea {
                        anchors.fill: parent

                        onPressed: {
                            prevX = mouseX
                            prevY = mouseY
                        }

                        onMouseXChanged: {
                            var dx = mouseX - prevX
                            mainWindow.setX(mainWindow.x + dx)
                        }

                        onMouseYChanged: {
                            var dy = mouseY - prevY
                            mainWindow.setY(mainWindow.y + dy)
                        }

                    }

                }

                Row {
                    Layout.alignment: Qt.AlignRight
                    Layout.fillHeight: true

                    Other.NavButton {
                        height: parent.height
                        text: "\uf5b0"

                        onClicked: mainWindow.showMinimized()

                    }

                    Other.NavButton {
                        height: parent.height
                        text: "\uF5af"

                    }

                    Other.NavButton {
                        height: parent.height
                        text: "\uF5ad"

                        onClicked: mainWindow.close()
                    }


                }

            }

        }
    }

    background: Rectangle {
        id: bg
        anchors.centerIn: parent
        width: mainWindow.width - 12
        height: mainWindow.height - 12
        color: "gold"

        layer.enabled: true
        /*layer.effect: DropShadow {
            anchors.fill: bg
            verticalOffset: 0
            horizontalOffset: 0
            radius: 12
            samples: 25
            color: "#80000000"
            source: bg
        }*/

    }

    Rectangle {
        id: adom
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.leftMargin: 6
        anchors.rightMargin: 6
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 6
        anchors.top: parent.top
        width: bg.width
        height: bg.height
        clip: true

        RowLayout {
            width: parent.width
            height: parent.height
            spacing: 0

            Rectangle { // Nav
                Layout.preferredWidth: 48
                Layout.fillHeight: true
                color: "black"

                Other.Nav {}

            }

            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: "white"

                ColumnLayout {
                    width: parent.width
                    height: parent.height
                    spacing: 0

                    DropArea {
                        Layout.fillWidth: true
                        Layout.fillHeight: true

                        onDropped: {
                            addfiles(drop.urls)
                        }

                        Rectangle {
                            anchors.fill: parent

                            ListView {
                                id: view
                                width: parent.width
                                height: parent.height
                                model: Comp.QmlFilesModel {}
                                delegate: Comp.QmlFilesDelegate {}
                                focus: true

                                ScrollBar.vertical: ScrollBar {}

                            }

                        }
                    }

                    Rectangle {
                        id: aligner
                        Layout.fillWidth: true
                        Layout.preferredHeight: 12
                        color: "#121316"
                    }

                    Rectangle {
                        id: infoPane
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        color: "white"

                        ListView {
                            id: infoView
                            anchors.fill: parent
                            spacing: 12
                            model: Comp.InfoModel {}
                            delegate: Comp.InfoDelegate {}
                            focus: true
                            clip: true

                            ScrollBar.vertical: ScrollBar {}
                            ScrollBar.horizontal: ScrollBar {}

                        }

                    }

                }
            }

        }

    }

    FileDialog {
        id: picker
        //selectExisting: true
        //selectMultiple: true
        //folder: shortcuts.home

        nameFilters: ['Qml Files (*.qml)']

        onAccepted: {
            addfiles(picker.fileUrls.toString())
        }

    }

    Timer {
        interval: 500; running: true; repeat: false
        onTriggered: bootUp('Loaded')
    }

    Connections {
        target: preview

        function onBootedUp(ret_val) {
            qt_version = ret_val
        }

        function onLog(ret_val) {

            var content
            var splits = ret_val.split(':::')
            var rel_ind = Number.parseFloat(splits[0])
            var main_data = splits[1]

            var prevCont = infoView.model.get(rel_ind).content

            if (prevCont === ''){
                content = main_data
            } else {
                content = prevCont + '<br/>' + main_data
            }

            console.log(rel_ind)
            infoView.model.setProperty(rel_ind, 'content', content)
            infoView.currentIndex = rel_ind
        }

        function onHotReloadExit(ind) {
            view.itemAtIndex(ind).setHotReloadMode()
        }

    }


}
