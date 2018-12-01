import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.3
import "others"
import "Components"

ApplicationWindow {
    width: 392
    height: 620
    visible: true

    property var fileUrls: []


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

        nameFilters: ['Qml File (*.qml)']

        onAccepted: {

            for (var x=0; x<picker.fileUrls.length; x++) {
                fileUrls.push(picker.fileUrls[x])
                console.log(picker.fileUrls[x])
            }

            console.log(fileUrls)
            console.log(picker.fileUrls.length)
        }

    }

}
