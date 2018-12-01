import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3
import "Component_Files"

ApplicationWindow {
    width: 392
    height: 620
    visible: true

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

}
