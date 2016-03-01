/********************************************************************************
** Form generated from reading UI file 'thirddialog.ui'
**
** Created: Mon Feb 15 20:21:41 2016
**      by: Qt User Interface Compiler version 4.8.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_THIRDDIALOG_H
#define UI_THIRDDIALOG_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QDialog>
#include <QtGui/QFrame>
#include <QtGui/QHeaderView>
#include <QtGui/QLCDNumber>
#include <QtGui/QLabel>
#include <QtGui/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_thirdDialog
{
public:
    QLabel *label;
    QLabel *label_2;
    QLCDNumber *lcdNumber;
    QPushButton *pushButton;
    QPushButton *pushButton_2;
    QLabel *label_3;
    QPushButton *pushButton_3;
    QLabel *label_4;
    QLCDNumber *lcdNumber_2;
    QPushButton *pushButton_4;
    QPushButton *pushButton_5;
    QLabel *label_8;
    QLabel *label_9;
    QFrame *line;
    QFrame *line_2;
    QFrame *line_3;
    QFrame *line_4;

    void setupUi(QDialog *thirdDialog)
    {
        if (thirdDialog->objectName().isEmpty())
            thirdDialog->setObjectName(QString::fromUtf8("thirdDialog"));
        thirdDialog->resize(800, 480);
        QFont font;
        font.setPointSize(18);
        thirdDialog->setFont(font);
        thirdDialog->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);"));
        label = new QLabel(thirdDialog);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(20, 0, 711, 111));
        label_2 = new QLabel(thirdDialog);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(220, 130, 301, 71));
        label_2->setStyleSheet(QString::fromUtf8("font: 22pt \"Times New Roman\";"));
        label_2->setAlignment(Qt::AlignCenter);
        lcdNumber = new QLCDNumber(thirdDialog);
        lcdNumber->setObjectName(QString::fromUtf8("lcdNumber"));
        lcdNumber->setGeometry(QRect(110, 240, 121, 81));
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
        lcdNumber->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 0, 0);"));
        pushButton = new QPushButton(thirdDialog);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setGeometry(QRect(290, 240, 51, 41));
        pushButton->setFont(font);
        pushButton_2 = new QPushButton(thirdDialog);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));
        pushButton_2->setGeometry(QRect(290, 290, 51, 41));
        QFont font1;
        font1.setPointSize(22);
        pushButton_2->setFont(font1);
        label_3 = new QLabel(thirdDialog);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(130, 330, 91, 21));
        label_3->setStyleSheet(QString::fromUtf8("font: 16pt \"Times New Roman\";"));
        label_3->setAlignment(Qt::AlignCenter);
        pushButton_3 = new QPushButton(thirdDialog);
        pushButton_3->setObjectName(QString::fromUtf8("pushButton_3"));
        pushButton_3->setGeometry(QRect(590, 230, 51, 41));
        pushButton_3->setFont(font);
        label_4 = new QLabel(thirdDialog);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setGeometry(QRect(430, 330, 91, 21));
        label_4->setStyleSheet(QString::fromUtf8("font: 16pt \"Times New Roman\";"));
        label_4->setAlignment(Qt::AlignCenter);
        lcdNumber_2 = new QLCDNumber(thirdDialog);
        lcdNumber_2->setObjectName(QString::fromUtf8("lcdNumber_2"));
        lcdNumber_2->setGeometry(QRect(410, 240, 121, 81));
        QPalette palette1;
        palette1.setBrush(QPalette::Active, QPalette::WindowText, brush);
        palette1.setBrush(QPalette::Active, QPalette::Button, brush);
        palette1.setBrush(QPalette::Active, QPalette::Light, brush);
        palette1.setBrush(QPalette::Active, QPalette::Text, brush);
        palette1.setBrush(QPalette::Active, QPalette::BrightText, brush);
        palette1.setBrush(QPalette::Active, QPalette::ButtonText, brush);
        palette1.setBrush(QPalette::Active, QPalette::Base, brush1);
        palette1.setBrush(QPalette::Active, QPalette::Window, brush1);
        palette1.setBrush(QPalette::Inactive, QPalette::WindowText, brush);
        palette1.setBrush(QPalette::Inactive, QPalette::Button, brush);
        palette1.setBrush(QPalette::Inactive, QPalette::Light, brush);
        palette1.setBrush(QPalette::Inactive, QPalette::Text, brush);
        palette1.setBrush(QPalette::Inactive, QPalette::BrightText, brush);
        palette1.setBrush(QPalette::Inactive, QPalette::ButtonText, brush);
        palette1.setBrush(QPalette::Inactive, QPalette::Base, brush1);
        palette1.setBrush(QPalette::Inactive, QPalette::Window, brush1);
        palette1.setBrush(QPalette::Disabled, QPalette::WindowText, brush2);
        palette1.setBrush(QPalette::Disabled, QPalette::Button, brush);
        palette1.setBrush(QPalette::Disabled, QPalette::Light, brush);
        palette1.setBrush(QPalette::Disabled, QPalette::Text, brush2);
        palette1.setBrush(QPalette::Disabled, QPalette::BrightText, brush);
        palette1.setBrush(QPalette::Disabled, QPalette::ButtonText, brush2);
        palette1.setBrush(QPalette::Disabled, QPalette::Base, brush1);
        palette1.setBrush(QPalette::Disabled, QPalette::Window, brush1);
        lcdNumber_2->setPalette(palette1);
        lcdNumber_2->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 0, 0);"));
        pushButton_4 = new QPushButton(thirdDialog);
        pushButton_4->setObjectName(QString::fromUtf8("pushButton_4"));
        pushButton_4->setGeometry(QRect(590, 280, 51, 41));
        pushButton_4->setFont(font1);
        pushButton_5 = new QPushButton(thirdDialog);
        pushButton_5->setObjectName(QString::fromUtf8("pushButton_5"));
        pushButton_5->setGeometry(QRect(320, 380, 91, 51));
        label_8 = new QLabel(thirdDialog);
        label_8->setObjectName(QString::fromUtf8("label_8"));
        label_8->setGeometry(QRect(240, 310, 47, 13));
        label_8->setStyleSheet(QString::fromUtf8("font: 75 12pt \"Times New Roman\";"));
        label_9 = new QLabel(thirdDialog);
        label_9->setObjectName(QString::fromUtf8("label_9"));
        label_9->setGeometry(QRect(540, 300, 47, 13));
        label_9->setStyleSheet(QString::fromUtf8("font: 75 12pt \"Times New Roman\";"));
        line = new QFrame(thirdDialog);
        line->setObjectName(QString::fromUtf8("line"));
        line->setGeometry(QRect(80, 205, 621, 31));
        line->setFrameShape(QFrame::HLine);
        line->setFrameShadow(QFrame::Sunken);
        line_2 = new QFrame(thirdDialog);
        line_2->setObjectName(QString::fromUtf8("line_2"));
        line_2->setGeometry(QRect(53, 220, 51, 251));
        line_2->setFrameShape(QFrame::VLine);
        line_2->setFrameShadow(QFrame::Sunken);
        line_3 = new QFrame(thirdDialog);
        line_3->setObjectName(QString::fromUtf8("line_3"));
        line_3->setGeometry(QRect(87, 449, 611, 31));
        line_3->setFrameShape(QFrame::HLine);
        line_3->setFrameShadow(QFrame::Sunken);
        line_4 = new QFrame(thirdDialog);
        line_4->setObjectName(QString::fromUtf8("line_4"));
        line_4->setGeometry(QRect(663, 220, 71, 241));
        line_4->setFrameShape(QFrame::VLine);
        line_4->setFrameShadow(QFrame::Sunken);

        retranslateUi(thirdDialog);
        QObject::connect(pushButton_5, SIGNAL(clicked()), thirdDialog, SLOT(close()));

        QMetaObject::connectSlotsByName(thirdDialog);
    } // setupUi

    void retranslateUi(QDialog *thirdDialog)
    {
        thirdDialog->setWindowTitle(QApplication::translate("thirdDialog", "Dialog", 0, QApplication::UnicodeUTF8));
        label->setText(QString());
        label_2->setText(QApplication::translate("thirdDialog", "POT\303\212NCIA ", 0, QApplication::UnicodeUTF8));
        pushButton->setText(QApplication::translate("thirdDialog", "+", 0, QApplication::UnicodeUTF8));
        pushButton_2->setText(QApplication::translate("thirdDialog", "-", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("thirdDialog", "Inicial", 0, QApplication::UnicodeUTF8));
        pushButton_3->setText(QApplication::translate("thirdDialog", "+", 0, QApplication::UnicodeUTF8));
        label_4->setText(QApplication::translate("thirdDialog", "Final", 0, QApplication::UnicodeUTF8));
        pushButton_4->setText(QApplication::translate("thirdDialog", "-", 0, QApplication::UnicodeUTF8));
        pushButton_5->setText(QApplication::translate("thirdDialog", "OK", 0, QApplication::UnicodeUTF8));
        label_8->setText(QApplication::translate("thirdDialog", "W", 0, QApplication::UnicodeUTF8));
        label_9->setText(QApplication::translate("thirdDialog", "W", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class thirdDialog: public Ui_thirdDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_THIRDDIALOG_H
