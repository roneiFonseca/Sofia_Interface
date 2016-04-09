/********************************************************************************
** Form generated from reading UI file 'monidialog.ui'
**
** Created by: Qt User Interface Compiler version 5.5.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MONIDIALOG_H
#define UI_MONIDIALOG_H

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

class Ui_moniDialog
{
public:
    QLabel *label_2;
    QLabel *label;
    QLabel *label_12;
    QLabel *label_14;
    QLabel *label_15;
    QPushButton *pushButton_7;
    QLabel *label_17;
    QLabel *label_20;
    QLCDNumber *lcdNumber_7;
    QLabel *label_21;
    QPushButton *pushButton_8;
    QLCDNumber *lcdNumber_8;
    QLabel *label_22;
    QLCDNumber *lcdNumber_9;
    QLabel *label_23;
    QLabel *label_24;
    QLabel *label_25;
    QLCDNumber *lcdNumber_10;
    QFrame *line;
    QFrame *line_2;
    QFrame *line_3;
    QFrame *line_4;
    QFrame *line_5;

    void setupUi(QDialog *moniDialog)
    {
        if (moniDialog->objectName().isEmpty())
            moniDialog->setObjectName(QStringLiteral("moniDialog"));
        moniDialog->resize(800, 480);
        moniDialog->setStyleSheet(QStringLiteral("background-color: rgb(255, 255, 255);"));
        label_2 = new QLabel(moniDialog);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(170, 120, 441, 71));
        label_2->setStyleSheet(QStringLiteral("font: 22pt \"Times New Roman\";"));
        label_2->setAlignment(Qt::AlignCenter);
        label = new QLabel(moniDialog);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(20, 0, 721, 111));
        label_12 = new QLabel(moniDialog);
        label_12->setObjectName(QStringLiteral("label_12"));
        label_12->setGeometry(QRect(650, 360, 91, 21));
        label_12->setStyleSheet(QStringLiteral("font: 16pt \"Times New Roman\";"));
        label_12->setAlignment(Qt::AlignCenter);
        label_14 = new QLabel(moniDialog);
        label_14->setObjectName(QStringLiteral("label_14"));
        label_14->setGeometry(QRect(650, 390, 47, 13));
        label_14->setStyleSheet(QStringLiteral("font: 75 12pt \"Times New Roman\";"));
        label_15 = new QLabel(moniDialog);
        label_15->setObjectName(QStringLiteral("label_15"));
        label_15->setGeometry(QRect(250, 430, 381, 16));
        QFont font;
        font.setPointSize(10);
        label_15->setFont(font);
        pushButton_7 = new QPushButton(moniDialog);
        pushButton_7->setObjectName(QStringLiteral("pushButton_7"));
        pushButton_7->setGeometry(QRect(20, 240, 141, 51));
        label_17 = new QLabel(moniDialog);
        label_17->setObjectName(QStringLiteral("label_17"));
        label_17->setGeometry(QRect(660, 260, 111, 21));
        label_17->setStyleSheet(QStringLiteral("font: 16pt \"Times New Roman\";"));
        label_17->setAlignment(Qt::AlignCenter);
        label_20 = new QLabel(moniDialog);
        label_20->setObjectName(QStringLiteral("label_20"));
        label_20->setGeometry(QRect(650, 290, 47, 13));
        label_20->setStyleSheet(QStringLiteral("font: 75 12pt \"Times New Roman\";"));
        lcdNumber_7 = new QLCDNumber(moniDialog);
        lcdNumber_7->setObjectName(QStringLiteral("lcdNumber_7"));
        lcdNumber_7->setGeometry(QRect(530, 340, 111, 71));
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
        lcdNumber_7->setPalette(palette);
        lcdNumber_7->setStyleSheet(QStringLiteral("background-color: rgb(0, 0, 0);"));
        label_21 = new QLabel(moniDialog);
        label_21->setObjectName(QStringLiteral("label_21"));
        label_21->setGeometry(QRect(170, 120, 441, 71));
        label_21->setStyleSheet(QStringLiteral("font: 22pt \"Times New Roman\";"));
        label_21->setAlignment(Qt::AlignCenter);
        pushButton_8 = new QPushButton(moniDialog);
        pushButton_8->setObjectName(QStringLiteral("pushButton_8"));
        pushButton_8->setGeometry(QRect(40, 350, 91, 51));
        QPalette palette1;
        palette1.setBrush(QPalette::Active, QPalette::WindowText, brush1);
        QBrush brush3(QColor(255, 255, 255, 255));
        brush3.setStyle(Qt::SolidPattern);
        palette1.setBrush(QPalette::Active, QPalette::Button, brush3);
        QBrush brush4(QColor(179, 179, 179, 255));
        brush4.setStyle(Qt::SolidPattern);
        palette1.setBrush(QPalette::Active, QPalette::Dark, brush4);
        palette1.setBrush(QPalette::Active, QPalette::Text, brush1);
        palette1.setBrush(QPalette::Active, QPalette::ButtonText, brush1);
        palette1.setBrush(QPalette::Active, QPalette::Base, brush3);
        palette1.setBrush(QPalette::Active, QPalette::Window, brush3);
        palette1.setBrush(QPalette::Inactive, QPalette::WindowText, brush1);
        palette1.setBrush(QPalette::Inactive, QPalette::Button, brush3);
        palette1.setBrush(QPalette::Inactive, QPalette::Dark, brush4);
        palette1.setBrush(QPalette::Inactive, QPalette::Text, brush1);
        palette1.setBrush(QPalette::Inactive, QPalette::ButtonText, brush1);
        palette1.setBrush(QPalette::Inactive, QPalette::Base, brush3);
        palette1.setBrush(QPalette::Inactive, QPalette::Window, brush3);
        palette1.setBrush(QPalette::Disabled, QPalette::WindowText, brush4);
        palette1.setBrush(QPalette::Disabled, QPalette::Button, brush3);
        palette1.setBrush(QPalette::Disabled, QPalette::Dark, brush4);
        palette1.setBrush(QPalette::Disabled, QPalette::Text, brush4);
        palette1.setBrush(QPalette::Disabled, QPalette::ButtonText, brush4);
        palette1.setBrush(QPalette::Disabled, QPalette::Base, brush3);
        palette1.setBrush(QPalette::Disabled, QPalette::Window, brush3);
        pushButton_8->setPalette(palette1);
        pushButton_8->setStyleSheet(QLatin1String("background-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);"));
        lcdNumber_8 = new QLCDNumber(moniDialog);
        lcdNumber_8->setObjectName(QStringLiteral("lcdNumber_8"));
        lcdNumber_8->setGeometry(QRect(530, 230, 111, 71));
        QPalette palette2;
        palette2.setBrush(QPalette::Active, QPalette::WindowText, brush);
        palette2.setBrush(QPalette::Active, QPalette::Button, brush);
        palette2.setBrush(QPalette::Active, QPalette::Light, brush);
        palette2.setBrush(QPalette::Active, QPalette::Text, brush);
        palette2.setBrush(QPalette::Active, QPalette::BrightText, brush);
        palette2.setBrush(QPalette::Active, QPalette::ButtonText, brush);
        palette2.setBrush(QPalette::Active, QPalette::Base, brush1);
        palette2.setBrush(QPalette::Active, QPalette::Window, brush1);
        palette2.setBrush(QPalette::Inactive, QPalette::WindowText, brush);
        palette2.setBrush(QPalette::Inactive, QPalette::Button, brush);
        palette2.setBrush(QPalette::Inactive, QPalette::Light, brush);
        palette2.setBrush(QPalette::Inactive, QPalette::Text, brush);
        palette2.setBrush(QPalette::Inactive, QPalette::BrightText, brush);
        palette2.setBrush(QPalette::Inactive, QPalette::ButtonText, brush);
        palette2.setBrush(QPalette::Inactive, QPalette::Base, brush1);
        palette2.setBrush(QPalette::Inactive, QPalette::Window, brush1);
        palette2.setBrush(QPalette::Disabled, QPalette::WindowText, brush2);
        palette2.setBrush(QPalette::Disabled, QPalette::Button, brush);
        palette2.setBrush(QPalette::Disabled, QPalette::Light, brush);
        palette2.setBrush(QPalette::Disabled, QPalette::Text, brush2);
        palette2.setBrush(QPalette::Disabled, QPalette::BrightText, brush);
        palette2.setBrush(QPalette::Disabled, QPalette::ButtonText, brush2);
        palette2.setBrush(QPalette::Disabled, QPalette::Base, brush1);
        palette2.setBrush(QPalette::Disabled, QPalette::Window, brush1);
        lcdNumber_8->setPalette(palette2);
        lcdNumber_8->setStyleSheet(QStringLiteral("background-color: rgb(0, 0, 0);"));
        label_22 = new QLabel(moniDialog);
        label_22->setObjectName(QStringLiteral("label_22"));
        label_22->setGeometry(QRect(380, 350, 111, 31));
        label_22->setStyleSheet(QStringLiteral("font: 16pt \"Times New Roman\";"));
        label_22->setAlignment(Qt::AlignCenter);
        lcdNumber_9 = new QLCDNumber(moniDialog);
        lcdNumber_9->setObjectName(QStringLiteral("lcdNumber_9"));
        lcdNumber_9->setGeometry(QRect(240, 330, 111, 71));
        QPalette palette3;
        palette3.setBrush(QPalette::Active, QPalette::WindowText, brush);
        palette3.setBrush(QPalette::Active, QPalette::Button, brush);
        palette3.setBrush(QPalette::Active, QPalette::Light, brush);
        palette3.setBrush(QPalette::Active, QPalette::Text, brush);
        palette3.setBrush(QPalette::Active, QPalette::BrightText, brush);
        palette3.setBrush(QPalette::Active, QPalette::ButtonText, brush);
        palette3.setBrush(QPalette::Active, QPalette::Base, brush1);
        palette3.setBrush(QPalette::Active, QPalette::Window, brush1);
        palette3.setBrush(QPalette::Active, QPalette::AlternateBase, brush1);
        palette3.setBrush(QPalette::Inactive, QPalette::WindowText, brush);
        palette3.setBrush(QPalette::Inactive, QPalette::Button, brush);
        palette3.setBrush(QPalette::Inactive, QPalette::Light, brush);
        palette3.setBrush(QPalette::Inactive, QPalette::Text, brush);
        palette3.setBrush(QPalette::Inactive, QPalette::BrightText, brush);
        palette3.setBrush(QPalette::Inactive, QPalette::ButtonText, brush);
        palette3.setBrush(QPalette::Inactive, QPalette::Base, brush1);
        palette3.setBrush(QPalette::Inactive, QPalette::Window, brush1);
        palette3.setBrush(QPalette::Inactive, QPalette::AlternateBase, brush1);
        palette3.setBrush(QPalette::Disabled, QPalette::WindowText, brush2);
        palette3.setBrush(QPalette::Disabled, QPalette::Button, brush);
        palette3.setBrush(QPalette::Disabled, QPalette::Light, brush);
        palette3.setBrush(QPalette::Disabled, QPalette::Text, brush2);
        palette3.setBrush(QPalette::Disabled, QPalette::BrightText, brush);
        palette3.setBrush(QPalette::Disabled, QPalette::ButtonText, brush2);
        palette3.setBrush(QPalette::Disabled, QPalette::Base, brush1);
        palette3.setBrush(QPalette::Disabled, QPalette::Window, brush1);
        palette3.setBrush(QPalette::Disabled, QPalette::AlternateBase, brush1);
        lcdNumber_9->setPalette(palette3);
        lcdNumber_9->setStyleSheet(QLatin1String("alternate-background-color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);"));
        label_23 = new QLabel(moniDialog);
        label_23->setObjectName(QStringLiteral("label_23"));
        label_23->setGeometry(QRect(360, 270, 47, 13));
        label_23->setStyleSheet(QStringLiteral("font: 75 12pt \"Times New Roman\";"));
        label_24 = new QLabel(moniDialog);
        label_24->setObjectName(QStringLiteral("label_24"));
        label_24->setGeometry(QRect(360, 380, 47, 13));
        label_24->setStyleSheet(QStringLiteral("font: 75 12pt \"Times New Roman\";"));
        label_25 = new QLabel(moniDialog);
        label_25->setObjectName(QStringLiteral("label_25"));
        label_25->setGeometry(QRect(370, 240, 91, 21));
        label_25->setStyleSheet(QStringLiteral("font: 16pt \"Times New Roman\";"));
        label_25->setAlignment(Qt::AlignCenter);
        lcdNumber_10 = new QLCDNumber(moniDialog);
        lcdNumber_10->setObjectName(QStringLiteral("lcdNumber_10"));
        lcdNumber_10->setGeometry(QRect(240, 230, 111, 71));
        QPalette palette4;
        palette4.setBrush(QPalette::Active, QPalette::WindowText, brush);
        palette4.setBrush(QPalette::Active, QPalette::Button, brush);
        palette4.setBrush(QPalette::Active, QPalette::Light, brush);
        palette4.setBrush(QPalette::Active, QPalette::Text, brush);
        palette4.setBrush(QPalette::Active, QPalette::BrightText, brush);
        palette4.setBrush(QPalette::Active, QPalette::ButtonText, brush);
        palette4.setBrush(QPalette::Active, QPalette::Base, brush1);
        palette4.setBrush(QPalette::Active, QPalette::Window, brush1);
        palette4.setBrush(QPalette::Inactive, QPalette::WindowText, brush);
        palette4.setBrush(QPalette::Inactive, QPalette::Button, brush);
        palette4.setBrush(QPalette::Inactive, QPalette::Light, brush);
        palette4.setBrush(QPalette::Inactive, QPalette::Text, brush);
        palette4.setBrush(QPalette::Inactive, QPalette::BrightText, brush);
        palette4.setBrush(QPalette::Inactive, QPalette::ButtonText, brush);
        palette4.setBrush(QPalette::Inactive, QPalette::Base, brush1);
        palette4.setBrush(QPalette::Inactive, QPalette::Window, brush1);
        palette4.setBrush(QPalette::Disabled, QPalette::WindowText, brush2);
        palette4.setBrush(QPalette::Disabled, QPalette::Button, brush);
        palette4.setBrush(QPalette::Disabled, QPalette::Light, brush);
        palette4.setBrush(QPalette::Disabled, QPalette::Text, brush2);
        palette4.setBrush(QPalette::Disabled, QPalette::BrightText, brush);
        palette4.setBrush(QPalette::Disabled, QPalette::ButtonText, brush2);
        palette4.setBrush(QPalette::Disabled, QPalette::Base, brush1);
        palette4.setBrush(QPalette::Disabled, QPalette::Window, brush1);
        lcdNumber_10->setPalette(palette4);
        lcdNumber_10->setStyleSheet(QStringLiteral("background-color: rgb(0, 0, 0);"));
        line = new QFrame(moniDialog);
        line->setObjectName(QStringLiteral("line"));
        line->setGeometry(QRect(7, 190, 731, 20));
        line->setFrameShape(QFrame::HLine);
        line->setFrameShadow(QFrame::Sunken);
        line_2 = new QFrame(moniDialog);
        line_2->setObjectName(QStringLiteral("line_2"));
        line_2->setGeometry(QRect(-7, 200, 31, 261));
        line_2->setFrameShape(QFrame::VLine);
        line_2->setFrameShadow(QFrame::Sunken);
        line_3 = new QFrame(moniDialog);
        line_3->setObjectName(QStringLiteral("line_3"));
        line_3->setGeometry(QRect(733, 200, 21, 271));
        line_3->setFrameShape(QFrame::VLine);
        line_3->setFrameShadow(QFrame::Sunken);
        line_4 = new QFrame(moniDialog);
        line_4->setObjectName(QStringLiteral("line_4"));
        line_4->setGeometry(QRect(10, 459, 731, 21));
        line_4->setFrameShape(QFrame::HLine);
        line_4->setFrameShadow(QFrame::Sunken);
        line_5 = new QFrame(moniDialog);
        line_5->setObjectName(QStringLiteral("line_5"));
        line_5->setGeometry(QRect(153, 200, 31, 261));
        line_5->setFrameShape(QFrame::VLine);
        line_5->setFrameShadow(QFrame::Sunken);

        retranslateUi(moniDialog);
        QObject::connect(pushButton_8, SIGNAL(clicked()), moniDialog, SLOT(close()));

        QMetaObject::connectSlotsByName(moniDialog);
    } // setupUi

    void retranslateUi(QDialog *moniDialog)
    {
        moniDialog->setWindowTitle(QApplication::translate("moniDialog", "Dialog", 0));
        label_2->setText(QApplication::translate("moniDialog", "TELA DE MONITORAMENTO", 0));
        label->setText(QString());
        label_12->setText(QApplication::translate("moniDialog", "Tempo", 0));
        label_14->setText(QApplication::translate("moniDialog", "min", 0));
        label_15->setText(QApplication::translate("moniDialog", "Status da Abla\303\247\303\243o: Iniciando/ Em andamento/ Finalizada ", 0));
        pushButton_7->setText(QApplication::translate("moniDialog", "CONFIGURA\303\207\303\225ES ", 0));
        label_17->setText(QApplication::translate("moniDialog", "Temperatura", 0));
        label_20->setText(QApplication::translate("moniDialog", "\302\272C", 0));
        label_21->setText(QApplication::translate("moniDialog", "TELA DE MONITORAMENTO", 0));
        pushButton_8->setText(QApplication::translate("moniDialog", "DESLIGAR", 0));
        label_22->setText(QApplication::translate("moniDialog", "Imped\303\242ncia", 0));
        label_23->setText(QApplication::translate("moniDialog", "W", 0));
        label_24->setText(QApplication::translate("moniDialog", "\316\251", 0));
        label_25->setText(QApplication::translate("moniDialog", "Pot\303\252ncia", 0));
    } // retranslateUi

};

namespace Ui {
    class moniDialog: public Ui_moniDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MONIDIALOG_H
