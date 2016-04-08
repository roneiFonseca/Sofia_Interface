/********************************************************************************
** Form generated from reading UI file 'fifdialog.ui'
**
** Created by: Qt User Interface Compiler version 5.4.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FIFDIALOG_H
#define UI_FIFDIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>

QT_BEGIN_NAMESPACE

class Ui_fifDialog
{
public:
    QLabel *label_2;
    QLabel *label;
    QPushButton *pushButton;
    QRadioButton *radioButton;
    QRadioButton *radioButton_2;
    QRadioButton *radioButton_3;

    void setupUi(QDialog *fifDialog)
    {
        if (fifDialog->objectName().isEmpty())
            fifDialog->setObjectName(QStringLiteral("fifDialog"));
        fifDialog->resize(634, 463);
        fifDialog->setStyleSheet(QStringLiteral("background-color: rgb(255, 255, 255);"));
        label_2 = new QLabel(fifDialog);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(150, 130, 301, 71));
        label_2->setStyleSheet(QStringLiteral("font: 22pt \"Times New Roman\";"));
        label_2->setAlignment(Qt::AlignCenter);
        label = new QLabel(fifDialog);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(0, 0, 681, 111));
        label->setPixmap(QPixmap(QString::fromUtf8("../untitled/imagens/teste.JPG")));
        pushButton = new QPushButton(fifDialog);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setGeometry(QRect(490, 360, 75, 23));
        radioButton = new QRadioButton(fifDialog);
        radioButton->setObjectName(QStringLiteral("radioButton"));
        radioButton->setGeometry(QRect(80, 200, 291, 51));
        radioButton_2 = new QRadioButton(fifDialog);
        radioButton_2->setObjectName(QStringLiteral("radioButton_2"));
        radioButton_2->setGeometry(QRect(80, 250, 291, 41));
        radioButton_3 = new QRadioButton(fifDialog);
        radioButton_3->setObjectName(QStringLiteral("radioButton_3"));
        radioButton_3->setGeometry(QRect(80, 310, 291, 21));

        retranslateUi(fifDialog);
        QObject::connect(pushButton, SIGNAL(clicked()), fifDialog, SLOT(close()));

        QMetaObject::connectSlotsByName(fifDialog);
    } // setupUi

    void retranslateUi(QDialog *fifDialog)
    {
        fifDialog->setWindowTitle(QApplication::translate("fifDialog", "Dialog", 0));
        label_2->setText(QApplication::translate("fifDialog", "MODO DE OPERA\303\207\303\203O", 0));
        label->setText(QString());
        pushButton->setText(QApplication::translate("fifDialog", "OK", 0));
        radioButton->setText(QApplication::translate("fifDialog", "MODO 1 (DEFAULT)  -  Step Pot.: 5 W T.: 2 min\n"
"", 0));
        radioButton_2->setText(QApplication::translate("fifDialog", "MODO 2 - Step Pot.: 10 W T.: 4 min", 0));
        radioButton_3->setText(QApplication::translate("fifDialog", "MODO 3 - Step Pot.: 2.5 W T.: 1 min\n"
"", 0));
    } // retranslateUi

};

namespace Ui {
    class fifDialog: public Ui_fifDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FIFDIALOG_H
