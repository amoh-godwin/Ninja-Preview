import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.5
import "../others"

Component {
    Rectangle {
        id: delebase
        width: parent.width
        height: 48
        color: index % 2 > 0 ? "white" : "#f1f1f1"

        RowLayout {
            width: parent.width - 8
            height: 40
            anchors.verticalCenter: parent.verticalCenter
            spacing: 0

            Text {
                padding: 8
                Layout.fillWidth: true
                text: name
                elide: Text.ElideMiddle
                font {
                    family: "Segoe UI Semilight"
                    pixelSize: 14
                }
            }

            CustomButton {
                text: "\uF40a"

                onClicked: runFile(name)

            }

            CustomButton {
                text: "\uF374"

                onClicked: removeFromView(index)

            }

        }


    }
}
