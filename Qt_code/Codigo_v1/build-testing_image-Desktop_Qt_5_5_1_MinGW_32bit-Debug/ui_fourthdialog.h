/********************************************************************************
** Form generated from reading UI file 'fourthdialog.ui'
**
** Created by: Qt User Interface Compiler version 5.5.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FOURTHDIALOG_H
#define UI_FOURTHDIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLCDNumber>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_fourthDialog
{
public:
    QPushButton *pushButton;
    QLabel *label_3;
    QLCDNumber *lcdNumber;
    QLabel *label_2;
    QLabel *label_4;
    QPushButton *pushButton_5;
    QLabel *label;
    QPushButton *pushButton_2;
    QLCDNumber *lcdNumber_2;
    QPushButton *pushButton_3;
    QPushButton *pushButton_4;
    QLabel *label_11;
    QLabel *label_12;
    QFrame *line;
    QFrame *line_2;
    QFrame *line_3;
    QFrame *line_4;
    QFrame *line_5;

    void setupUi(QDialog *fourthDialog)
    {
        if (fourthDialog->objectName().isEmpty())
            fourthDialog->setObjectName(QStringLiteral("fourthDialog"));
        fourthDialog->resize(800, 465);
        fourthDialog->setStyleSheet(QStringLiteral("background-color: rgb(255, 255, 255);"));
        pushButton = new QPushButton(fourthDialog);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setGeometry(QRect(290, 240, 51, 41));
        QFont font;
        font.setPointSize(18);
        pushButton->setFont(font);
        label_3 = new QLabel(fourthDialog);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(140, 330, 91, 21));
        label_3->setStyleSheet(QStringLiteral("font: 16pt \"Times New Roman\";"));
        label_3->setAlignment(Qt::AlignCenter);
        lcdNumber = new QLCDNumber(fourthDialog);
        lcdNumber->setObjectName(QStringLiteral("lcdNumber"));
        lcdNumber->setGeometry(QRect(130, 240, 111, 81));
        QPalette palette;
        QBrush brush(QColor(0, 0, 255, 255));
        brush.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::WindowText, brush);
        palette.setBrush(QPalette::Active, QPalette::Button, brush);
        palette.setBrush(QPalette::Active, QPalette::Light, brush);
        palette.setBrush(QPalette::Active, QPalette::Text, brush);
        palette.setBrush(QPalette::Active, QPalette::BrightText, brush);
        palette.setBrush(QPalette::Active, QPalette::ButtonText, brush);
        QBrush brush1(QColor(0, 0, 0, 255));
        brush1.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Base, brush1);
        palette.setBrush(QPalette::Active, QPalette::Window, brush1);
        palette.setBrush(QPalette::Inactive, QPalette::WindowText, brush);
        palette.setBrush(QPalette::Inactive, QPalette::Button, brush);
        palette.setBrush(QPalette::Inactive, QPalette::Light, brush);
        palette.setBrush(QPalette::Inactive, QPalette::Text, brush);
        palette.setBrush(QPalette::Inactive, QPalette::BrightText, brush);
        palette.setBrush(QPalette::Inactive, QPalette::ButtonText, brush);
        palette.setBrush(QPalette::Inactive, QPalette::Base, brush1);
        palette.setBrush(QPalette::Inactive, QPalette::Window, brush1);
        QBrush brush2(QColor(120, 120, 120, 255));
        brush2.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Disabled, QPalette::WindowText, brush2);
        palette.setBrush(QPalette::Disabled, QPalette::Button, brush);
        palette.setBrush(QPalette::Disabled, QPalette::Light, brush);
        palette.setBrush(QPalette::Disabled, QPalette::Text, brush2);
        palette.setBrush(QPalette::Disabled, QPalette::BrightText, brush);
        palette.setBrush(QPalette::Disabled, QPalette::ButtonText, brush2);
        palette.setBrush(QPalette::Disabled, QPalette::Base, brush1);
        palette.setBrush(QPalette::Disabled, QPalette::Window, brush1);
        lcdNumber->setPalette(palette);
        lcdNumber->setStyleSheet(QStringLiteral("background-color: rgb(0, 0, 0);"));
        label_2 = new QLabel(fourthDialog);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(230, 130, 301, 71));
        QFont font1;
        font1.setFamily(QStringLiteral("Times New Roman"));
        font1.setPointSize(22);
        font1.setBold(false);
        font1.setItalic(false);
        font1.setWeight(50);
        label_2->setFont(font1);
        label_2->setStyleSheet(QStringLiteral("font: 22pt \"Times New Roman\";"));
        label_2->setAlignment(Qt::AlignCenter);
        label_4 = new QLabel(fourthDialog);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setGeometry(QRect(480, 330, 91, 21));
        label_4->setStyleSheet(QStringLiteral("font: 16pt \"Times New Roman\";"));
        label_4->setAlignment(Qt::AlignCenter);
        pushButton_5 = new QPushButton(fourthDialog);
        pushButton_5->setObjectName(QStringLiteral("pushButton_5"));
        pushButton_5->setGeometry(QRect(350, 390, 91, 51));
        label = new QLabel(fourthDialog);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(10, 10, 711, 111));
        pushButton_2 = new QPushButton(fourthDialog);
        pushButton_2->setObjectName(QStringLiteral("pushButton_2"));
        pushButton_2->setGeometry(QRect(290, 290, 51, 41));
        QFont font2;
        font2.setPointSize(22);
        pushButton_2->setFont(font2);
        lcdNumber_2 = new QLCDNumber(fourthDialog);
        lcdNumber_2->setObjectName(QStringLiteral("lcdNumber_2"));
        lcdNumber_2->setGeometry(QRect(450, 240, 121, 81));
        QPalette palette1;
        QBrush brush3(QColor(255, 0, 0, 255));
        brush3.setStyle(Qt::SolidPattern);
        palette1.setBrush(QPalette::Active, QPalette::WindowText, brush3);
        palette1.setBrush(QPalette::Active, QPalette::Button, brush3);
        palette1.setBrush(QPalette::Active, QPalette::Light, brush3);
        palette1.setBrush(QPalette::Active, QPalette::Text, brush3);
        palette1.setBrush(QPalette::Active, QPalette::BrightText, brush3);
        palette1.setBrush(QPalette::Active, QPalette::ButtonText, brush3);
        palette1.setBrush(QPalette::Active, QPalette::Base, brush1);
        palette1.setBrush(QPalette::Active, QPalette::Window, brush1);
        palette1.setBrush(QPalette::Inactive, QPalette::WindowText, brush3);
        palette1.setBrush(QPalette::Inactive, QPalette::Button, brush3);
        palette1.setBrush(QPalette::Inactive, QPalette::Light, brush3);
        palette1.setBrush(QPalette::Inactive, QPalette::Text, brush3);
        palette1.setBrush(QPalette::Inactive, QPalette::BrightText, brush3);
        palette1.setBrush(QPalette::Inactive, QPalette::ButtonText, brush3);
        palette1.setBrush(QPalette::Inactive, QPalette::Base, brush1);
        palette1.setBrush(QPalette::Inactive, QPalette::Window, brush1);
        palette1.setBrush(QPalette::Disabled, QPalette::WindowText, brush2);
        palette1.setBrush(QPalette::Disabled, QPalette::Button, brush3);
        palette1.setBrush(QPalette::Disabled, QPalette::Light, brush3);
        palette1.setBrush(QPalette::Disabled, QPalette::Text, brush2);
        palette1.setBrush(QPalette::Disabled, QPalette::BrightText, brush3);
        palette1.setBrush(QPalette::Disabled, QPalette::ButtonText, brush2);
        palette1.setBrush(QPalette::Disabled, QPalette::Base, brush1);
        palette1.setBrush(QPalette::Disabled, QPalette::Window, brush1);
        lcdNumber_2->setPalette(palette1);
        lcdNumber_2->setStyleSheet(QStringLiteral("background-color: rgb(0, 0, 0);"));
        pushButton_3 = new QPushButton(fourthDialog);
        pushButton_3->setObjectName(QStringLiteral("pushButton_3"));
        pushButton_3->setGeometry(QRect(610, 240, 51, 41));
        pushButton_3->setFont(font);
        pushButton_4 = new QPushButton(fourthDialog);
        pushButton_4->setObjectName(QStringLiteral("pushButton_4"));
        pushButton_4->setGeometry(QRect(610, 290, 51, 41));
        pushButton_4->setFont(font2);
        label_11 = new QLabel(fourthDialog);
        label_11->setObjectName(QStringLiteral("label_11"));
        label_11->setGeometry(QRect(250, 290, 31, 16));
        label_11->setStyleSheet(QStringLiteral("font: 75 12pt \"Times New Roman\";"));
        label_12 = new QLabel(fourthDialog);
        label_12->setObjectName(QStringLiteral("label_12"));
        label_12->setGeometry(QRect(580, 300, 21, 16));
        label_12->setStyleSheet(QStringLiteral("font: 75 12pt \"Times New Roman\";"));
        line = new QFrame(fourthDialog);
        line->setObjectName(QStringLiteral("line"));
        line->setGeometry(QRect(30, 190, 701, 41));
        line->setFrameShape(QFrame::HLine);
        line->setFrameShadow(QFrame::Sunken);
        line_2 = new QFrame(fourthDialog);
        line_2->setObjectName(QStringLiteral("line_2"));
        line_2->setGeometry(QRect(20, 210, 20, 251));
        line_2->setFrameShape(QFrame::VLine);
        line_2->setFrameShadow(QFrame::Sunken);
        line_3 = new QFrame(fourthDialog);
        line_3->setObjectName(QStringLiteral("line_3"));
        line_3->setGeometry(QRect(390, 230, 16, 141));
        line_3->setFrameShape(QFrame::VLine);
        line_3->setFrameShadow(QFrame::Sunken);
        line_4 = new QFrame(fourthDialog);
        line_4->setObjectName(QStringLiteral("line_4"));
        line_4->setGeometry(QRect(30, 450, 701, 20));
        line_4->setFrameShape(QFrame::HLine);
        line_4->setFrameShadow(QFrame::Sunken);
        line_5 = new QFrame(fourthDialog);
        line_5->setObjectName(QStringLiteral("line_5"));
        line_5->setGeometry(QRect(720, 210, 20, 251));
        line_5->setFrameShape(QFrame::VLine);
        line_5->setFrameShadow(QFrame::Sunken);

        retranslateUi(fourthDialog);
        QObject::connect(pushButton_5, SIGNAL(clicked()), fourthDialog, SLOT(close()));

        QMetaObject::connectSlotsByName(fourthDialog);
    } // setupUi

    void retranslateUi(QDialog *fourthDialog)
    {
        fourthDialog->setWindowTitle(QApplication::translate("fourthDialog", "Dialog", 0));
        pushButton->setText(QApplication::translate("fourthDialog", "+", 0));
        label_3->setText(QApplication::translate("fourthDialog", "Inicial", 0));
        label_2->setText(QApplication::translate("fourthDialog", "TEMPO", 0));
        label_4->setText(QApplication::translate("fourthDialog", "Final", 0));
        pushButton_5->setText(QApplication::translate("fourthDialog", "OK", 0));
        label->setText(QString());
        pushButton_2->setText(QApplication::translate("fourthDialog", "-", 0));
        pushButton_3->setText(QApplication::translate("fourthDialog", "+", 0));
        pushButton_4->setText(QApplication::translate("fourthDialog", "-", 0));
        label_11->setText(QApplication::translate("fourthDialog", "min", 0));
        label_12->setText(QApplication::translate("fourthDialog", "min", 0));
    } // retranslateUi

};

namespace Ui {
    class fourthDialog: public Ui_fourthDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FOURTHDIALOG_H
