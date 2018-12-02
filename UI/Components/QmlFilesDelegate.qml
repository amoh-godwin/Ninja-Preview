import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3

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

            Button {
                anchors.verticalCenter: parent.verticalCenter
                Layout.preferredWidth: 36
                Layout.preferredHeight: 28
                font.family: "Segoe MDL2 Assets"
                text: "\uE768"

                background: Rectangle {
                    implicitWidth: 36
                    implicitHeight: 28
                    color: parent.pressed ? "#c1c1c1" : parent.hovered ? "#e1e1e1" : "transparent"
                }

                contentItem: Text {
                    verticalAlignment: Text.AlignVCenter
                    horizontalAlignment: Text.AlignHCenter
                    text: parent.text
                    font: parent.font
                    color: "green"
                }

            }

            Button {
                anchors.verticalCenter: parent.verticalCenter
                Layout.preferredWidth: 36
                Layout.preferredHeight: 28
                text: "\uE711"
            }

        }


    }
}
