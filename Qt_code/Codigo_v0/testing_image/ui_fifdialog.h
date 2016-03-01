/********************************************************************************
** Form generated from reading UI file 'fifdialog.ui'
**
** Created: Mon Feb 15 20:21:42 2016
**      by: Qt User Interface Compiler version 4.8.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FIFDIALOG_H
#define UI_FIFDIALOG_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QDialog>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QPushButton>
#include <QtGui/QRadioButton>

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
            fifDialog->setObjectName(QString::fromUtf8("fifDialog"));
        fifDialog->resize(800, 480);
        QFont font;
        font.setFamily(QString::fromUtf8("Times New Roman"));
        font.setPointSize(22);
        font.setBold(true);
        font.setItalic(false);
        font.setWeight(75);
        fifDialog->setFont(font);
        fifDialog->setFocusPolicy(Qt::NoFocus);
        fifDialog->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);"));
        label_2 = new QLabel(fifDialog);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(230, 140, 301, 71));
        QFont font1;
        font1.setFamily(QString::fromUtf8("Times New Roman"));
        font1.setPointSize(22);
        font1.setBold(false);
        font1.setItalic(false);
        font1.setWeight(50);
        label_2->setFont(font1);
        label_2->setStyleSheet(QString::fromUtf8("font: 22pt \"Times New Roman\";"));
        label_2->setTextFormat(Qt::PlainText);
        label_2->setAlignment(Qt::AlignCenter);
        label = new QLabel(fifDialog);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(20, 0, 721, 111));
        pushButton = new QPushButton(fifDialog);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setGeometry(QRect(340, 350, 101, 51));
        QFont font2;
        font2.setPointSize(9);
        pushButton->setFont(font2);
        radioButton = new QRadioButton(fifDialog);
        radioButton->setObjectName(QString::fromUtf8("radioButton"));
        radioButton->setGeometry(QRect(40, 220, 351, 51));
        QFont font3;
        font3.setPointSize(11);
        radioButton->setFont(font3);
        radioButton_2 = new QRadioButton(fifDialog);
        radioButton_2->setObjectName(QString::fromUtf8("radioButton_2"));
        radioButton_2->setGeometry(QRect(40, 270, 291, 41));
        radioButton_2->setFont(font3);
        radioButton_3 = new QRadioButton(fifDialog);
        radioButton_3->setObjectName(QString::fromUtf8("radioButton_3"));
        radioButton_3->setGeometry(QRect(40, 320, 291, 31));
        radioButton_3->setFont(font3);

        retranslateUi(fifDialog);
        QObject::connect(pushButton, SIGNAL(clicked()), fifDialog, SLOT(close()));

        QMetaObject::connectSlotsByName(fifDialog);
    } // setupUi

    void retranslateUi(QDialog *fifDialog)
    {
        fifDialog->setWindowTitle(QApplication::translate("fifDialog", "Dialog", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("fifDialog", "MODO DE OPERA\303\207\303\203O", 0, QApplication::UnicodeUTF8));
        label->setText(QString());
        pushButton->setText(QApplication::translate("fifDialog", "OK", 0, QApplication::UnicodeUTF8));
        radioButton->setText(QApplication::translate("fifDialog", "MODO 1 - Step Pot.: 5 W T .: 2 min", 0, QApplication::UnicodeUTF8));
        radioButton_2->setText(QApplication::translate("fifDialog", "MODO 2 - Step Pot.: 10 W T.: 4 min", 0, QApplication::UnicodeUTF8));
        radioButton_3->setText(QApplication::translate("fifDialog", "MODO 3 - Step Pot.: 2.5 W T.: 1 min", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class fifDialog: public Ui_fifDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FIFDIALOG_H
