import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.5

Component {
    ColumnLayout {
        width: parent.width
        Rectangle {
            Layout.fillWidth: true
            //Layout.minimumHeight: 24
            Layout.preferredHeight: textChild.height
            color: "white"

            Text {
                id: textChild
                width: parent.width
                wrapMode: Text.WordWrap
                textFormat: Text.RichText
                font.family: "Segoe UI Semilight"
                font.pixelSize: 14
                text: "[ " + index +" ] :    " + content
            }

        }
    }
}
