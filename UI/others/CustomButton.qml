import QtQuick
import QtQuick.Controls.Basic
import QtQuick.Layouts

Button {

    property bool style_up: false

    Layout.alignment: Layout.Center
    Layout.preferredWidth: 36
    Layout.preferredHeight: 28
    font.family: __main__font__.name
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
        style: parent.style_up ? Text.Outline : Text.Normal
        styleColor: "dodgerblue"
        color: parent.style_up ? "transparent" : "green"
    }

}
