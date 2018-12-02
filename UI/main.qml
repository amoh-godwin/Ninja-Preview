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

    signal addfiles(string ctnt)

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
