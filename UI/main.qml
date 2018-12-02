import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.3
import "others"
import "Components"

ApplicationWindow {
    id: mainWindow
    width: 392
    height: 620
    visible: true

    flags: Qt.Window | Qt.FramelessWindowHint

    property int prevX
    property int prevY

    signal addfiles(string ctnt)
    signal removeFromView(int index)
    signal runFile(string filename)

    onAddfiles: {

        var filelist = ctnt.split(',')
        var len = filelist.length

        while (len > 0) {
            var url = filelist[len - 1]
            var name = url.substring(8, url.length)
            view.model.append({"url": url, "name": name})
            len--
        }

    }

    onRemoveFromView: {
        view.model.remove(index)
    }

    onRunFile: {
        //
    }


    header: Rectangle {
        width: parent.width
        height: 36
        color: "#191b1f"

        RowLayout {
            height: parent.height

            Image {
                anchors.left: parent.left
                anchors.leftMargin: 15
                anchors.verticalCenter: parent.verticalCenter
                sourceSize.width: 18
                sourceSize.height: 18
                source: "icons/ic_airplay_white_18dp.png"
            }

            Text {
                anchors.left: parent.children[0].right
                anchors.leftMargin: 15
                font {
                    family: "Segoe UI Semilight"
                    pixelSize: 14
                }

                text: "Ninja-Preview"
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

    Rectangle {
        anchors.fill: parent

        RowLayout {
            width: parent.width
            height: parent.height
            spacing: 0

            Rectangle {
                Layout.preferredWidth: 48
                Layout.fillHeight: true
                color: "black"

                Nav {}

            }

            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: "white"

                ListView {
                    id: view
                    width: parent.width
                    height: parent.height
                    model: QmlFilesModel {}
                    delegate: QmlFilesDelegate {}
                    focus: true

                    ScrollBar.vertical: ScrollBar {}

                }

            }

        }


    }

    FileDialog {
        id: picker
        selectExisting: true
        selectMultiple: true

        nameFilters: ['Qml Files (*.qml)']

        onAccepted: {
            addfiles(picker.fileUrls.toString())
        }

    }

}
