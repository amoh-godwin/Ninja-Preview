import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3
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
                text: "\uE768"

                onClicked: runFile(name)

            }

            CustomButton {
                text: "\uE738"

                onClicked: removeFromView(index)

            }

        }


    }
}
