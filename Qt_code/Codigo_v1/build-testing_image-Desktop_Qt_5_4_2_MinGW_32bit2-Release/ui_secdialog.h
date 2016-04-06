/********************************************************************************
** Form generated from reading UI file 'secdialog.ui'
**
** Created by: Qt User Interface Compiler version 5.4.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SECDIALOG_H
#define UI_SECDIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>

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
            SecDialog->setObjectName(QStringLiteral("SecDialog"));
        SecDialog->resize(639, 414);
        SecDialog->setStyleSheet(QStringLiteral("background-color: rgb(255, 255, 255);"));
        label = new QLabel(SecDialog);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(0, -10, 681, 111));
        label->setPixmap(QPixmap(QString::fromUtf8("../untitled/imagens/teste.JPG")));
        label_2 = new QLabel(SecDialog);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(170, 120, 301, 71));
        label_2->setStyleSheet(QStringLiteral("font: 22pt \"Times New Roman\";"));
        label_2->setAlignment(Qt::AlignCenter);
        pushButton_4 = new QPushButton(SecDialog);
        pushButton_4->setObjectName(QStringLiteral("pushButton_4"));
        pushButton_4->setGeometry(QRect(200, 360, 91, 41));
        pushButton_4->setStyleSheet(QStringLiteral("border-color: rgb(0, 0, 0);"));
        pushButton_5 = new QPushButton(SecDialog);
        pushButton_5->setObjectName(QStringLiteral("pushButton_5"));
        pushButton_5->setGeometry(QRect(360, 360, 91, 41));
        pushButton_5->setStyleSheet(QStringLiteral("border-color: rgb(0, 0, 0);"));
        pushButton_6 = new QPushButton(SecDialog);
        pushButton_6->setObjectName(QStringLiteral("pushButton_6"));
        pushButton_6->setGeometry(QRect(240, 290, 151, 41));
        pushButton_7 = new QPushButton(SecDialog);
        pushButton_7->setObjectName(QStringLiteral("pushButton_7"));
        pushButton_7->setGeometry(QRect(240, 210, 151, 31));
        pushButton_8 = new QPushButton(SecDialog);
        pushButton_8->setObjectName(QStringLiteral("pushButton_8"));
        pushButton_8->setGeometry(QRect(240, 250, 151, 31));

        retranslateUi(SecDialog);

        QMetaObject::connectSlotsByName(SecDialog);
    } // setupUi

    void retranslateUi(QDialog *SecDialog)
    {
        SecDialog->setWindowTitle(QApplication::translate("SecDialog", "Dialog", 0));
        label->setText(QString());
        label_2->setText(QApplication::translate("SecDialog", "CONFIGURA\303\207\303\225ES", 0));
        pushButton_4->setText(QApplication::translate("SecDialog", "Iniciar", 0));
        pushButton_5->setText(QApplication::translate("SecDialog", "Desligar", 0));
        pushButton_6->setText(QApplication::translate("SecDialog", "MODO DE OPERA\303\207\303\203O", 0));
        pushButton_7->setText(QApplication::translate("SecDialog", "POT\303\212NCIA", 0));
        pushButton_8->setText(QApplication::translate("SecDialog", "TEMPO", 0));
    } // retranslateUi

};

namespace Ui {
    class SecDialog: public Ui_SecDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SECDIALOG_H
