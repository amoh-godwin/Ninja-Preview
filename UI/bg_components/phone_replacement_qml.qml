import QtQuick
import QtQuick.Controls.Basic
import QtQuick.Layouts
import "qrc:///UI/others" as Other

ApplicationWindow {
    id: main__window
    visible: true
    width: 468
    height: 736
    title: "{MainWindowItem}"
    color: "transparent"
    flags: Qt.Window | Qt.FramelessWindowHint
    objectName: "MainWindowItem"

    signal switchFrame(string name)

    Component.onCompleted: {
        var x = (screen.width - width) / 2
        var y = (screen.desktopAvailableHeight - height) / 2
        setX(x)
        setY(y)
    }

    onSwitchFrame: {
        if (name == "huawei_SL") {
            var anc = "top: 44, bottom: 52, left: 24, right: 84"
            sam_s_u_n_g.visible = false
            hu__a_w_e_i.visible = true
            main__window.setWidth(468)
            main__window.setHeight(736)

            // set margins
            ff__.anchors.topMargin = 44
            ff__.anchors.bottomMargin = 52
            ff__.anchors.leftMargin = 24
            ff__.anchors.rightMargin = 84

            var x = (screen.width - 468) / 2
            var y = (screen.desktopAvailableHeight - 736) / 2
            main__window.setX(x)
            main__window.setY(y)

            __back__ground__.curr_device = 'huawei'
        } else if (name == "samsung_u") {
            var anch = "top: 60, bottom: 60, left: 68, right: 130"
            hu__a_w_e_i.visible = false
            sam_s_u_n_g.visible = true
            main__window.setWidth(995)
            main__window.setHeight(670)

            // set margins
            ff__.anchors.topMargin = 35
            ff__.anchors.bottomMargin = 35
            ff__.anchors.leftMargin = 71
            ff__.anchors.rightMargin = 124

            var tx = (screen.width - 995) / 2
            var ty = (screen.desktopAvailableHeight - 670) / 2
            main__window.setX(tx)
            main__window.setY(ty)

            __back__ground__.curr_device = 'samsung'
        }
    }

    FontLoader { id: __main__font__; source: "qrc:///UI/fonts/materialdesignicons/materialdesignicons-webfont.ttf" }

    background: Rectangle {
        id: __back__ground__
        anchors.fill: parent
        color: "transparent"

        property string curr_device: "huawei"

        RowLayout {
            anchors.fill: parent
            spacing:  12

            Rectangle {
                id: hu__a_w_e_i
                Layout.fillWidth: true
                Layout.fillHeight: true
                Layout.leftMargin: 6
                color: "transparent"
                visible: true

                Image {
                    width: parent.width
                    height: parent.height
                    source: "qrc:///images/Huawei_SL.png"
                }

                Rectangle {
                    id: to_p_b_a_r
                    width: parent.width
                    height: 44
                    color: "transparent"

                    property int prevX
                    property int prevY

                    MouseArea {
                        anchors.fill: parent

                        onPressed: {
                            to_p_b_a_r.prevX = mouseX
                            to_p_b_a_r.prevY = mouseY
                        }

                        onMouseXChanged: {
                            var dx = mouseX - to_p_b_a_r.prevX
                            main__window.setX(main__window.x + dx)
                        }

                        onMouseYChanged: {
                            var dy = mouseY - to_p_b_a_r.prevY
                            main__window.setY(main__window.y + dy)
                        }

                    }

                }

            }

            Rectangle {
                id: sam_s_u_n_g
                Layout.fillWidth: true
                Layout.fillHeight: true
                Layout.leftMargin: 6
                color: "transparent"
                visible: false

                Image {
                    width: parent.width
                    height: parent.height
                    source: "qrc:///images/ipad.png"
                }

                Rectangle {
                    id: _to_p_b_a_r
                    width: parent.width
                    height: 60
                    color: "transparent"

                    property int prevX
                    property int prevY

                    MouseArea {
                        anchors.fill: parent

                        onPressed: {
                            _to_p_b_a_r.prevX = mouseX
                            _to_p_b_a_r.prevY = mouseY
                        }

                        onMouseXChanged: {
                            var dx = mouseX - _to_p_b_a_r.prevX
                            main__window.setX(main__window.x + dx)
                        }

                        onMouseYChanged: {
                            var dy = mouseY - _to_p_b_a_r.prevY
                            main__window.setY(main__window.y + dy)
                        }

                    }

                }

            }

            Rectangle {
                Layout.preferredWidth: 48
                Layout.fillHeight: true
                color: "black"

                ToolBar {
                    width: parent.width
                    height: parent.height

                    background: Rectangle {
                        color: "#191b1f"
                    }

                    ColumnLayout {
                        width: parent.width
                        //height: parent.height

                        Other.NavButton {
                            text: "\uFa34"
                            enabled: __back__ground__.curr_device != 'huawei'

                            onClicked: switchFrame('huawei_SL')

                        }

                        Other.NavButton {
                            text: "\uF41e"
                            enabled: __back__ground__.curr_device != 'samsung'

                            onClicked: switchFrame('samsung_u')

                        }

                    }

                }
            }


        }



    }

    Rectangle {
        id: ff__
        anchors.fill: parent
        anchors.topMargin: 44
        anchors.bottomMargin: 52
        anchors.leftMargin: 24
        anchors.rightMargin: 84
        clip: true
        color: "black"

        ColumnLayout {
            anchors.fill: parent
            clip: true
            spacing: 0

            Rectangle {// menubar
                id: _hidd_me_nu_bar
                Layout.fillWidth: true
                Layout.preferredHeight: (children.length > 0) ? children[0].height : 48
                visible: (children.length > 0)
                clip: true
                color: "transparent"
                objectName: "menuBarContainerItem"


            }

            Rectangle {// header
                id: _hidd_he_ad_er
                Layout.fillWidth: true
                Layout.preferredHeight: (children.length > 0) ? children[0].height : 48
                visible: (children.length > 0)
                clip: true
                color: "transparent"
                objectName: "headerItem"


            }

            Rectangle {// contentItem
                id: _hidd_co_nt_entItem
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: "{ContentItem}"
                clip: true
                objectName: "ContentItem"


            }

            Rectangle {// footer
                id: _hidd_fo_ot_er
                Layout.fillWidth: true
                Layout.preferredHeight: (children.length > 0) ? children[0].height : 48
                visible: (children.length > 0)
                color: "transparent"
                clip: true
                objectName: "footerItem"


            }

        }
    }

}
