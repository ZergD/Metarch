import QtQuick 2.6
import QtQuick.Layouts 1.2
import QtQuick.Controls 1.2
import QtQuick.Window 2.1
import QtQuick.Dialogs 1.2

Rectangle{
    id: screen

    antialiasing: true

    width: 800
    height: 600
    color: "#63676e"
    visible: true
    //    color: "black"

    gradient: Gradient{
        GradientStop { position: 0.0; color: "#180d28" }
        //        GradientStop { position: 0.0; color: "#0c1727" }
        //        GradientStop { position: 0.7; color: "#032759" }
        GradientStop { position: 1.0; color: "#001029" }
    }

    Rectangle {
        id: top_bar
        x: 0
        y: 0
        width: parent.width
        height: 40
        color: "#181727"
        z: 1
        border.color: "gray"
        border.width: 2

        Item {
            id: columnBox
            x: 116
            y: 0
            width: 397
            height: 40
            clip: false
            visible: true
            transformOrigin: Item.TopLeft

            Text {
                id: menu
                width: 107
                height: parent.height
                color: "#fdfdfd"
                text: qsTr("Menu")
                transformOrigin: Item.Center
                anchors.top: parent.top
                anchors.topMargin: 0
                horizontalAlignment: Text.AlignHCenter
                font.pixelSize: 12
                verticalAlignment: Text.AlignVCenter
                onActiveFocusChanged: {
                    color: "red"
                }


            }

            Text {
                id: element2
                x: 112
                y: 0
                width: 107
                height: parent.height
                color: "#f9f9f9"
                text: qsTr("Option")
                transformOrigin: Item.Center
                anchors.top: parent.top
                anchors.topMargin: 0
                horizontalAlignment: Text.AlignHCenter
                font.pixelSize: 12
                verticalAlignment: Text.AlignVCenter
            }

            Text {
                id: element3
                x: 229
                y: 0
                width: 107
                height: parent.height
                color: "#ffffff"
                text: qsTr("Profile")
                transformOrigin: Item.Center
                horizontalAlignment: Text.AlignHCenter
                font.pixelSize: 12
                verticalAlignment: Text.AlignVCenter
            }
        }

    }

    Rectangle {
        id: sidebar
        x: 0
        y: 38

        width: 117
        height: 562
        //    color: "steelblue"
        color: "#001029"
        z: 1
        border.color: "gray"
        border.width: 2

        Text {
            id: menu1
            x: 5
            y: 216
            width: 107
            height: 49
            color: "#fdfdfd"
            text: qsTr("Send & Simulate")
            z: 4
            anchors.top: parent.top
            horizontalAlignment: Text.AlignHCenter
            transformOrigin: Item.Center
            anchors.topMargin: 0
            font.pixelSize: 12
            verticalAlignment: Text.AlignVCenter
        }

        Text {
            id: menu2
            x: 5
            y: 207
            width: 107
            height: 49
            color: "#fdfdfd"
            text: qsTr("Inspect Jobs")
            anchors.top: parent.top
            horizontalAlignment: Text.AlignHCenter
            font.pixelSize: 12
            anchors.topMargin: 55
            transformOrigin: Item.Center
            z: 4
            verticalAlignment: Text.AlignVCenter
        }

    }

    Text {
        id: element
        x: 329
        y: 90
        width: 397
        height: 32
        color: "#e0bdbd"
        text: qsTr("Name of the Starting Foldcer : ")
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignLeft
        font.pixelSize: 12
    }

    Button {
        id: button
        x: 162
        y: 88
        width: 125
        height: 36
        text: qsTr("Open Start Folder")

        onClicked: fileDialog.open()

    }

    Text {
        id: element1
        x: 329
        y: 161
        width: 107
        height: 32
        color: "#e0bdbd"
        text: qsTr("Name: ")
        horizontalAlignment: Text.AlignHCenter
        font.pixelSize: 12
        verticalAlignment: Text.AlignVCenter
    }

    Button {
        id: button1
        x: 162
        y: 159
        width: 125
        height: 36
        text: qsTr("Finished Folder")
    }

    FileDialog{
        id: fileDialog
        selectMultiple: true
        selectFolder: true

        onAccepted: {
            element.text = this.fileUrl
        }
    }

    Button {
        id: button2
        x: 162
        y: 515
        width: 220
        height: 62
        text: qsTr("RUN")
    }



}



















//import QtQuick 2.10
//import QtQuick.Controls 2.3
//import QtQuick.Layouts 1.3
//
//ApplicationWindow {
//    id: mainWindow
//    width: 400
//    height: 400
//    title: qsTr("Frameless")
//    property int previousX
//    property int previousY
//
//    Rectangle {
//        width: parent.width
//        height: 40
//        color: "gold"
//
//        anchors.top: parent.top
//
//        Text {
//            anchors.verticalCenter: parent.verticalCenter
//            leftPadding: 8
//            text: mainWindow.title
//            color: "white"
//        }
//
//        MouseArea {
//            anchors.fill: parent
//
//            onPressed: {
//                previousX = mouseX
//                previousY = mouseY
//            }
//
//            onMouseXChanged: {
//                var dx = mouseX - previousX
//                mainWindow.setX(mainWindow.x + dx)
//            }
//
//            onMouseYChanged: {
//                var dy = mouseY - previousY
//                mainWindow.setY(mainWindow.y + dy)
//            }
//
//        }
//
//    }
//
//    MouseArea {
//        width: 5
//
//        anchors {
//            right: parent.right
//            top: parent.top
//            bottom: parent.bottom
//        }
//
//        cursorShape: Qt.SizeHorCursor
//
//        onPressed: previousX = mouseX
//
//        onMouseXChanged: {
//            var dx = mouseX - previousX
//            mainWindow.setWidth(parent.width + dx)
//        }
//
//    }
//
//    MouseArea {
//        height: 5
//        anchors {
//            top: parent.top
//            left: parent.left
//            right: parent.right
//        }
//
//        cursorShape: Qt.SizeVerCursor
//
//        onPressed: previousY = mouseY
//
//        onMouseYChanged: {
//            var dy = mouseY - previousY
//            mainWindow.setY(mainWindow.y + dy)
//            mainWindow.setHeight(mainWindow.height - dy)
//
//        }
//    }
//}
























//    Item {
//        width: parent.width
//        anchors { top: parent.top; bottom: toolBar.top }
//
//        Image {
//            id: background_main
//            anchors.fill: parent
//            source: "C:\Users\marcm\Pictures\brainpicture.jpg"
//            fillMode: Image.PreserveAspectCrop
//        }
//    }

//    FileDialog {
//        id: fileDialog
//        title: "Please choose a file"
//        folder: shortcuts.home
//        onAccepted: {
//            console.log("You chose: " + fileDialog.fileUrls)
//            Qt.quit()
//        }
//        onRejected: {
//            console.log("Cancelled")
//            Qt.quit()
//        }
//        Component.onCompleted: visible = true
//    }



//    anchor.top : background.bottom

//}


//Rectangle {
//    id: mainScreen
//
//    property int currentIndex: 0
//
//    width: 400
//    height: 400
//
//    color: "white"
//
//    ListView {
//        id: listview
//        anchors.fill: parent
////        orientation: ListView.Vertical
//        orientation: ListView.Horizontal
//
//        model: colorModel
//
//        delegate: Rectangle {
//            height: colorText.height + 20
//            width: parent.width
//            color: modelData
//            Text {
//                id: colorText
//                text: modelData
//                font.pixelSize: 20
//                anchors.horizontalCenter: parent.horizontalCenter
//                anchors.verticalCenter: parent.verticalCenter
//            }
//        }
//    }
//
//}

//Rectangle{
//id: top_bar
//
//width: parent.width
//height: 40
//color: activePalette.window
//
//}
//

