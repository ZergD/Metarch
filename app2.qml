import QtQuick 2.3
import QtQuick.Layouts 1.3
import QtQuick.Dialogs.qml 1.0
import QtGraphicalEffects 1.0
import QtQuick.Extras 1.4
import QtQuick.Controls.Styles.Desktop 1.0
import QtQuick.Controls 1.6
import QtQuick.Window 2.10
import QtTest 1.2


Item {
    id: window
    width: 320
    height: 480

    Rectangle{
        id: background

        width: 320
        height: 480

        color: "darkgray"
    }

    Item {
        id: window2
        width: 320
        height: 480

        Rectangle{
            id: background2

            width: 320
            height: 480

            color: "#dafbf7"

            StatusIndicator {
                id: statusIndicator
                x: 45
                y: 62
            }

            Dial {
                id: dial
                x: 158
                y: 23
            }

            Gauge {
                id: gauge
                x: 236
                y: 149
            }

            ToggleButton {
                id: toggleButton
                x: 38
                y: 279
                text: qsTr("Button")
            }

            Tumbler {
                id: tumbler
                x: 179
                y: 301
                z: 5
            }
        }
    }
}

