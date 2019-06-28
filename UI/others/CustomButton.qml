import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12

Button {
    Layout.alignment: Layout.Center
    Layout.preferredWidth: 36
    Layout.preferredHeight: 28
    font.family: "Material Design Icons"
    font.pixelSize: 16

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
