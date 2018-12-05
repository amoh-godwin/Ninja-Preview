import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.3
import "others"
import "Components"

ApplicationWindow {
    id: mainWindow
    width: 800
    height: 600
    visible: true
    title: "C:/path/to/qmlfile.qml"

    flags: Qt.Window | Qt.FramelessWindowHint

    property int prevX
    property int prevY

    signal addfiles(string ctnt)
    signal removeFromView(int index)
    signal runFile(string filename)

    onAddfiles: {

        var filelist = ctnt.split(',')
        var len = filelist.length

        while (len > 0) {
            var url = filelist[len - 1]
            var name = url.substring(8, url.length)
            view.model.append({"url": url, "name": name})
            len--
        }

    }

    onRemoveFromView: {
        view.model.remove(index)
    }

    onRunFile: {
        // call the python code to run the filename
        preview.run(filename)
    }


    header: Rectangle {
        width: parent.width
        height: 36
        color: "#191b1f"

        RowLayout {
            height: parent.height

            Image {
                Layout.leftMargin: 15
                Layout.alignment: Layout.Center
                sourceSize.width: 18
                sourceSize.height: 18
                source: "icons/ic_airplay_white_18dp.png"
            }

            Text {
                Layout.leftMargin: 15
                width: 200
                font {
                    family: "Segoe UI Semilight"
                    pixelSize: 12
                }
                elide: Text.ElideMiddle
                text: title
                color: "white"
            }

            Text {
                font {
                    family: "Segoe UI Semilight"
                    pixelSize: 12
                }
                text: " -  Ninja-Preview (64-bit)"
                color: "white"
            }

        }

        MouseArea {
            anchors.fill: parent

            onPressed: {
                prevX = mouseX
                prevY = mouseY
            }

            onMouseXChanged: {
                var dx = mouseX - prevX
                mainWindow.setX(mainWindow.x + dx)
            }

            onMouseYChanged: {
                var dy = mouseY - prevY
                mainWindow.setY(mainWindow.y + dy)
            }

        }
    }

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

                ColumnLayout {
                    width: parent.width
                    height: parent.height
                    spacing: 0

                    Rectangle {
                        Layout.fillWidth: true
                        Layout.fillHeight: true

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

                    Rectangle {
                        id: aligner
                        Layout.fillWidth: true
                        Layout.preferredHeight: 12
                        color: "#121316"
                    }

                    Rectangle {
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        color: "white"

                        ListView {
                            width: parent.width
                            height: parent.height
                            spacing: 8
                            model: 8
                            delegate: InfoDelegate {}
                            focus: true
                            clip: true

                            ScrollBar.vertical: ScrollBar {}
                            ScrollBar.horizontal: ScrollBar {}

                        }

                    }

                }
            }

        }


    }

    FileDialog {
        id: picker
        selectExisting: true
        selectMultiple: true

        nameFilters: ['Qml Files (*.qml)']

        onAccepted: {
            addfiles(picker.fileUrls.toString())
        }

    }

    Connections {
        target: preview
    }

}
