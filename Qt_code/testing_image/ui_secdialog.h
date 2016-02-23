/********************************************************************************
** Form generated from reading UI file 'secdialog.ui'
**
** Created: Mon Feb 15 20:21:41 2016
**      by: Qt User Interface Compiler version 4.8.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SECDIALOG_H
#define UI_SECDIALOG_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QDialog>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_SecDialog
{
public:
    QLabel *label;
    QLabel *label_2;
    QPushButton *pushButton_4;
    QPushButton *pushButton_5;
    QPushButton *pushButton_6;
    QPushButton *pushButton_7;
    QPushButton *pushButton_8;

    void setupUi(QDialog *SecDialog)
    {
        if (SecDialog->objectName().isEmpty())
            SecDialog->setObjectName(QString::fromUtf8("SecDialog"));
        SecDialog->resize(800, 480);
        SecDialog->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);"));
        label = new QLabel(SecDialog);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(10, 10, 721, 111));
        label_2 = new QLabel(SecDialog);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(260, 130, 301, 71));
        label_2->setStyleSheet(QString::fromUtf8("font: 22pt \"Times New Roman\";"));
        label_2->setAlignment(Qt::AlignCenter);
        pushButton_4 = new QPushButton(SecDialog);
        pushButton_4->setObjectName(QString::fromUtf8("pushButton_4"));
        pushButton_4->setGeometry(QRect(210, 340, 91, 61));
        pushButton_4->setStyleSheet(QString::fromUtf8("border-color: rgb(0, 0, 0);"));
        pushButton_5 = new QPushButton(SecDialog);
        pushButton_5->setObjectName(QString::fromUtf8("pushButton_5"));
        pushButton_5->setGeometry(QRect(400, 340, 101, 61));
        pushButton_5->setStyleSheet(QString::fromUtf8("border-color: rgb(0, 0, 0);"));
        pushButton_6 = new QPushButton(SecDialog);
        pushButton_6->setObjectName(QString::fromUtf8("pushButton_6"));
        pushButton_6->setGeometry(QRect(530, 220, 161, 61));
        pushButton_7 = new QPushButton(SecDialog);
        pushButton_7->setObjectName(QString::fromUtf8("pushButton_7"));
        pushButton_7->setGeometry(QRect(80, 220, 161, 61));
        pushButton_8 = new QPushButton(SecDialog);
        pushButton_8->setObjectName(QString::fromUtf8("pushButton_8"));
        pushButton_8->setGeometry(QRect(300, 220, 161, 61));

        retranslateUi(SecDialog);
        QObject::connect(pushButton_5, SIGNAL(clicked()), SecDialog, SLOT(close()));

        QMetaObject::connectSlotsByName(SecDialog);
    } // setupUi

    void retranslateUi(QDialog *SecDialog)
    {
        SecDialog->setWindowTitle(QApplication::translate("SecDialog", "Dialog", 0, QApplication::UnicodeUTF8));
        label->setText(QString());
        label_2->setText(QApplication::translate("SecDialog", "CONFIGURA\303\207\303\225ES", 0, QApplication::UnicodeUTF8));
        pushButton_4->setText(QApplication::translate("SecDialog", "Iniciar", 0, QApplication::UnicodeUTF8));
        pushButton_5->setText(QApplication::translate("SecDialog", "Desligar", 0, QApplication::UnicodeUTF8));
        pushButton_6->setText(QApplication::translate("SecDialog", "MODO DE OPERA\303\207\303\203O", 0, QApplication::UnicodeUTF8));
        pushButton_7->setText(QApplication::translate("SecDialog", "POT\303\212NCIA", 0, QApplication::UnicodeUTF8));
        pushButton_8->setText(QApplication::translate("SecDialog", "TEMPO", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class SecDialog: public Ui_SecDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SECDIALOG_H
