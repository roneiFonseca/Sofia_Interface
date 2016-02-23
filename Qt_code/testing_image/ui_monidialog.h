/********************************************************************************
** Form generated from reading UI file 'monidialog.ui'
**
** Created: Mon Feb 15 22:08:28 2016
**      by: Qt User Interface Compiler version 4.8.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MONIDIALOG_H
#define UI_MONIDIALOG_H

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

class Ui_moniDialog
{
public:
    QLabel *label_2;
    QLabel *label;
    QLabel *label_14;
    QLabel *label_15;
    QPushButton *pushButton_7;
    QLabel *label_20;
    QLCDNumber *lcd_tempo;
    QLabel *label_21;
    QPushButton *pushButton_8;
    QLCDNumber *lcd_temp;
    QLCDNumber *lcd_imp;
    QLabel *label_23;
    QLabel *label_24;
    QLCDNumber *lcd_potencia;
    QFrame *line;
    QFrame *line_2;
    QFrame *line_3;
    QFrame *line_4;
    QFrame *line_5;

    void setupUi(QDialog *moniDialog)
    {
        if (moniDialog->objectName().isEmpty())
            moniDialog->setObjectName(QString::fromUtf8("moniDialog"));
        moniDialog->resize(800, 480);
        moniDialog->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);"));
        label_2 = new QLabel(moniDialog);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(170, 120, 441, 71));
        label_2->setStyleSheet(QString::fromUtf8("font: 22pt \"Times New Roman\";"));
        label_2->setAlignment(Qt::AlignCenter);
        label = new QLabel(moniDialog);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(20, 0, 721, 111));
        label_14 = new QLabel(moniDialog);
        label_14->setObjectName(QString::fromUtf8("label_14"));
        label_14->setGeometry(QRect(650, 390, 47, 13));
        QFont font;
        font.setFamily(QString::fromUtf8("Times New Roman"));
        font.setPointSize(12);
        font.setBold(false);
        font.setItalic(false);
        font.setWeight(9);
        label_14->setFont(font);
        label_14->setStyleSheet(QString::fromUtf8("font: 75 12pt \"Times New Roman\";"));
        label_15 = new QLabel(moniDialog);
        label_15->setObjectName(QString::fromUtf8("label_15"));
        label_15->setGeometry(QRect(250, 430, 381, 16));
        QFont font1;
        font1.setPointSize(10);
        label_15->setFont(font1);
        pushButton_7 = new QPushButton(moniDialog);
        pushButton_7->setObjectName(QString::fromUtf8("pushButton_7"));
        pushButton_7->setGeometry(QRect(20, 240, 141, 51));
        label_20 = new QLabel(moniDialog);
        label_20->setObjectName(QString::fromUtf8("label_20"));
        label_20->setGeometry(QRect(650, 290, 47, 13));
        label_20->setFont(font);
        label_20->setStyleSheet(QString::fromUtf8("font: 75 12pt \"Times New Roman\";"));
        lcd_tempo = new QLCDNumber(moniDialog);
        lcd_tempo->setObjectName(QString::fromUtf8("lcd_tempo"));
        lcd_tempo->setGeometry(QRect(530, 340, 111, 71));
        QPalette palette;
        QBrush brush(QColor(0, 0, 255, 255));
        brush.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::WindowText, brush);
        QBrush brush1(QColor(0, 0, 0, 255));
        brush1.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Button, brush1);
        palette.setBrush(QPalette::Active, QPalette::Light, brush);
        palette.setBrush(QPalette::Active, QPalette::Text, brush);
        palette.setBrush(QPalette::Active, QPalette::BrightText, brush);
        palette.setBrush(QPalette::Active, QPalette::ButtonText, brush);
        palette.setBrush(QPalette::Active, QPalette::Base, brush1);
        palette.setBrush(QPalette::Active, QPalette::Window, brush1);
        palette.setBrush(QPalette::Inactive, QPalette::WindowText, brush);
        palette.setBrush(QPalette::Inactive, QPalette::Button, brush1);
        palette.setBrush(QPalette::Inactive, QPalette::Light, brush);
        palette.setBrush(QPalette::Inactive, QPalette::Text, brush);
        palette.setBrush(QPalette::Inactive, QPalette::BrightText, brush);
        palette.setBrush(QPalette::Inactive, QPalette::ButtonText, brush);
        palette.setBrush(QPalette::Inactive, QPalette::Base, brush1);
        palette.setBrush(QPalette::Inactive, QPalette::Window, brush1);
        QBrush brush2(QColor(120, 120, 120, 255));
        brush2.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Disabled, QPalette::WindowText, brush2);
        palette.setBrush(QPalette::Disabled, QPalette::Button, brush1);
        palette.setBrush(QPalette::Disabled, QPalette::Light, brush);
        palette.setBrush(QPalette::Disabled, QPalette::Text, brush2);
        palette.setBrush(QPalette::Disabled, QPalette::BrightText, brush);
        palette.setBrush(QPalette::Disabled, QPalette::ButtonText, brush2);
        palette.setBrush(QPalette::Disabled, QPalette::Base, brush1);
        palette.setBrush(QPalette::Disabled, QPalette::Window, brush1);
        lcd_tempo->setPalette(palette);
        lcd_tempo->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 0, 0);"));
        label_21 = new QLabel(moniDialog);
        label_21->setObjectName(QString::fromUtf8("label_21"));
        label_21->setGeometry(QRect(170, 120, 441, 71));
        label_21->setStyleSheet(QString::fromUtf8("font: 22pt \"Times New Roman\";"));
        label_21->setAlignment(Qt::AlignCenter);
        pushButton_8 = new QPushButton(moniDialog);
        pushButton_8->setObjectName(QString::fromUtf8("pushButton_8"));
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
        pushButton_8->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);"));
        lcd_temp = new QLCDNumber(moniDialog);
        lcd_temp->setObjectName(QString::fromUtf8("lcd_temp"));
        lcd_temp->setGeometry(QRect(530, 230, 111, 71));
        QPalette palette2;
        palette2.setBrush(QPalette::Active, QPalette::WindowText, brush);
        palette2.setBrush(QPalette::Active, QPalette::Button, brush1);
        palette2.setBrush(QPalette::Active, QPalette::Light, brush);
        palette2.setBrush(QPalette::Active, QPalette::Text, brush);
        palette2.setBrush(QPalette::Active, QPalette::BrightText, brush);
        palette2.setBrush(QPalette::Active, QPalette::ButtonText, brush);
        palette2.setBrush(QPalette::Active, QPalette::Base, brush1);
        palette2.setBrush(QPalette::Active, QPalette::Window, brush1);
        palette2.setBrush(QPalette::Inactive, QPalette::WindowText, brush);
        palette2.setBrush(QPalette::Inactive, QPalette::Button, brush1);
        palette2.setBrush(QPalette::Inactive, QPalette::Light, brush);
        palette2.setBrush(QPalette::Inactive, QPalette::Text, brush);
        palette2.setBrush(QPalette::Inactive, QPalette::BrightText, brush);
        palette2.setBrush(QPalette::Inactive, QPalette::ButtonText, brush);
        palette2.setBrush(QPalette::Inactive, QPalette::Base, brush1);
        palette2.setBrush(QPalette::Inactive, QPalette::Window, brush1);
        palette2.setBrush(QPalette::Disabled, QPalette::WindowText, brush2);
        palette2.setBrush(QPalette::Disabled, QPalette::Button, brush1);
        palette2.setBrush(QPalette::Disabled, QPalette::Light, brush);
        palette2.setBrush(QPalette::Disabled, QPalette::Text, brush2);
        palette2.setBrush(QPalette::Disabled, QPalette::BrightText, brush);
        palette2.setBrush(QPalette::Disabled, QPalette::ButtonText, brush2);
        palette2.setBrush(QPalette::Disabled, QPalette::Base, brush1);
        palette2.setBrush(QPalette::Disabled, QPalette::Window, brush1);
        lcd_temp->setPalette(palette2);
        lcd_temp->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 0, 0);"));
        lcd_imp = new QLCDNumber(moniDialog);
        lcd_imp->setObjectName(QString::fromUtf8("lcd_imp"));
        lcd_imp->setGeometry(QRect(240, 330, 111, 71));
        QPalette palette3;
        palette3.setBrush(QPalette::Active, QPalette::WindowText, brush);
        palette3.setBrush(QPalette::Active, QPalette::Button, brush1);
        palette3.setBrush(QPalette::Active, QPalette::Light, brush);
        palette3.setBrush(QPalette::Active, QPalette::Text, brush);
        palette3.setBrush(QPalette::Active, QPalette::BrightText, brush);
        palette3.setBrush(QPalette::Active, QPalette::ButtonText, brush);
        palette3.setBrush(QPalette::Active, QPalette::Base, brush1);
        palette3.setBrush(QPalette::Active, QPalette::Window, brush1);
        palette3.setBrush(QPalette::Active, QPalette::AlternateBase, brush1);
        palette3.setBrush(QPalette::Inactive, QPalette::WindowText, brush);
        palette3.setBrush(QPalette::Inactive, QPalette::Button, brush1);
        palette3.setBrush(QPalette::Inactive, QPalette::Light, brush);
        palette3.setBrush(QPalette::Inactive, QPalette::Text, brush);
        palette3.setBrush(QPalette::Inactive, QPalette::BrightText, brush);
        palette3.setBrush(QPalette::Inactive, QPalette::ButtonText, brush);
        palette3.setBrush(QPalette::Inactive, QPalette::Base, brush1);
        palette3.setBrush(QPalette::Inactive, QPalette::Window, brush1);
        palette3.setBrush(QPalette::Inactive, QPalette::AlternateBase, brush1);
        palette3.setBrush(QPalette::Disabled, QPalette::WindowText, brush2);
        palette3.setBrush(QPalette::Disabled, QPalette::Button, brush1);
        palette3.setBrush(QPalette::Disabled, QPalette::Light, brush);
        palette3.setBrush(QPalette::Disabled, QPalette::Text, brush2);
        palette3.setBrush(QPalette::Disabled, QPalette::BrightText, brush);
        palette3.setBrush(QPalette::Disabled, QPalette::ButtonText, brush2);
        palette3.setBrush(QPalette::Disabled, QPalette::Base, brush1);
        palette3.setBrush(QPalette::Disabled, QPalette::Window, brush1);
        palette3.setBrush(QPalette::Disabled, QPalette::AlternateBase, brush1);
        lcd_imp->setPalette(palette3);
        lcd_imp->setStyleSheet(QString::fromUtf8("alternate-background-color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);"));
        label_23 = new QLabel(moniDialog);
        label_23->setObjectName(QString::fromUtf8("label_23"));
        label_23->setGeometry(QRect(360, 270, 47, 13));
        label_23->setFont(font);
        label_23->setStyleSheet(QString::fromUtf8("font: 75 12pt \"Times New Roman\";"));
        label_24 = new QLabel(moniDialog);
        label_24->setObjectName(QString::fromUtf8("label_24"));
        label_24->setGeometry(QRect(360, 380, 47, 13));
        label_24->setFont(font);
        label_24->setStyleSheet(QString::fromUtf8("font: 75 12pt \"Times New Roman\";"));
        lcd_potencia = new QLCDNumber(moniDialog);
        lcd_potencia->setObjectName(QString::fromUtf8("lcd_potencia"));
        lcd_potencia->setGeometry(QRect(240, 230, 111, 71));
        QPalette palette4;
        palette4.setBrush(QPalette::Active, QPalette::WindowText, brush);
        palette4.setBrush(QPalette::Active, QPalette::Button, brush1);
        palette4.setBrush(QPalette::Active, QPalette::Light, brush);
        palette4.setBrush(QPalette::Active, QPalette::Text, brush);
        palette4.setBrush(QPalette::Active, QPalette::BrightText, brush);
        palette4.setBrush(QPalette::Active, QPalette::ButtonText, brush);
        palette4.setBrush(QPalette::Active, QPalette::Base, brush1);
        palette4.setBrush(QPalette::Active, QPalette::Window, brush1);
        palette4.setBrush(QPalette::Inactive, QPalette::WindowText, brush);
        palette4.setBrush(QPalette::Inactive, QPalette::Button, brush1);
        palette4.setBrush(QPalette::Inactive, QPalette::Light, brush);
        palette4.setBrush(QPalette::Inactive, QPalette::Text, brush);
        palette4.setBrush(QPalette::Inactive, QPalette::BrightText, brush);
        palette4.setBrush(QPalette::Inactive, QPalette::ButtonText, brush);
        palette4.setBrush(QPalette::Inactive, QPalette::Base, brush1);
        palette4.setBrush(QPalette::Inactive, QPalette::Window, brush1);
        palette4.setBrush(QPalette::Disabled, QPalette::WindowText, brush2);
        palette4.setBrush(QPalette::Disabled, QPalette::Button, brush1);
        palette4.setBrush(QPalette::Disabled, QPalette::Light, brush);
        palette4.setBrush(QPalette::Disabled, QPalette::Text, brush2);
        palette4.setBrush(QPalette::Disabled, QPalette::BrightText, brush);
        palette4.setBrush(QPalette::Disabled, QPalette::ButtonText, brush2);
        palette4.setBrush(QPalette::Disabled, QPalette::Base, brush1);
        palette4.setBrush(QPalette::Disabled, QPalette::Window, brush1);
        lcd_potencia->setPalette(palette4);
        lcd_potencia->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 0, 0);"));
        line = new QFrame(moniDialog);
        line->setObjectName(QString::fromUtf8("line"));
        line->setGeometry(QRect(7, 190, 731, 20));
        line->setFrameShape(QFrame::HLine);
        line->setFrameShadow(QFrame::Sunken);
        line_2 = new QFrame(moniDialog);
        line_2->setObjectName(QString::fromUtf8("line_2"));
        line_2->setGeometry(QRect(-7, 200, 31, 261));
        line_2->setFrameShape(QFrame::VLine);
        line_2->setFrameShadow(QFrame::Sunken);
        line_3 = new QFrame(moniDialog);
        line_3->setObjectName(QString::fromUtf8("line_3"));
        line_3->setGeometry(QRect(733, 200, 21, 271));
        line_3->setFrameShape(QFrame::VLine);
        line_3->setFrameShadow(QFrame::Sunken);
        line_4 = new QFrame(moniDialog);
        line_4->setObjectName(QString::fromUtf8("line_4"));
        line_4->setGeometry(QRect(10, 459, 731, 21));
        line_4->setFrameShape(QFrame::HLine);
        line_4->setFrameShadow(QFrame::Sunken);
        line_5 = new QFrame(moniDialog);
        line_5->setObjectName(QString::fromUtf8("line_5"));
        line_5->setGeometry(QRect(153, 200, 31, 261));
        line_5->setFrameShape(QFrame::VLine);
        line_5->setFrameShadow(QFrame::Sunken);

        retranslateUi(moniDialog);
        QObject::connect(pushButton_8, SIGNAL(clicked()), moniDialog, SLOT(close()));

        QMetaObject::connectSlotsByName(moniDialog);
    } // setupUi

    void retranslateUi(QDialog *moniDialog)
    {
        moniDialog->setWindowTitle(QApplication::translate("moniDialog", "Dialog", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("moniDialog", "TELA DE MONITORAMENTO", 0, QApplication::UnicodeUTF8));
        label->setText(QString());
        label_14->setText(QApplication::translate("moniDialog", "min", 0, QApplication::UnicodeUTF8));
        label_15->setText(QApplication::translate("moniDialog", "Status da Abla\303\247\303\243o: Iniciando/ Em andamento/ Finalizada ", 0, QApplication::UnicodeUTF8));
        pushButton_7->setText(QApplication::translate("moniDialog", "CONFIGURA\303\207\303\225ES ", 0, QApplication::UnicodeUTF8));
        label_20->setText(QApplication::translate("moniDialog", "\302\272C", 0, QApplication::UnicodeUTF8));
        label_21->setText(QApplication::translate("moniDialog", "TELA DE MONITORAMENTO", 0, QApplication::UnicodeUTF8));
        pushButton_8->setText(QApplication::translate("moniDialog", "DESLIGAR", 0, QApplication::UnicodeUTF8));
        label_23->setText(QApplication::translate("moniDialog", "W", 0, QApplication::UnicodeUTF8));
        label_24->setText(QApplication::translate("moniDialog", "\316\251", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class moniDialog: public Ui_moniDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MONIDIALOG_H
