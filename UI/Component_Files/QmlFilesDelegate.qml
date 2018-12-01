import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3

Component {
    Rectangle {
        width: parent.width
        height: 48

        RowLayout {
            width: parent.width
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
                Layout.preferredHeight: 36
                text: ">"
            }

            Button {
                anchors.verticalCenter: parent.verticalCenter
                Layout.preferredWidth: 36
                Layout.preferredHeight: 36
                text: "x"
            }

        }


    }
}
