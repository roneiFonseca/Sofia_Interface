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

    void setupUi(QDialog *fourthDialog)
    {
        if (fourthDialog->objectName().isEmpty())
            fourthDialog->setObjectName(QStringLiteral("fourthDialog"));
        fourthDialog->resize(526, 415);
        fourthDialog->setStyleSheet(QStringLiteral("background-color: rgb(255, 255, 255);"));
        pushButton = new QPushButton(fourthDialog);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setGeometry(QRect(130, 240, 51, 41));
        label_3 = new QLabel(fourthDialog);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(50, 200, 91, 21));
        label_3->setStyleSheet(QStringLiteral("font: 16pt \"Times New Roman\";"));
        label_3->setAlignment(Qt::AlignCenter);
        lcdNumber = new QLCDNumber(fourthDialog);
        lcdNumber->setObjectName(QStringLiteral("lcdNumber"));
        lcdNumber->setGeometry(QRect(10, 260, 71, 51));
        label_2 = new QLabel(fourthDialog);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(110, 120, 301, 71));
        label_2->setStyleSheet(QStringLiteral("font: 22pt \"Times New Roman\";"));
        label_2->setAlignment(Qt::AlignCenter);
        label_4 = new QLabel(fourthDialog);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setGeometry(QRect(390, 200, 91, 21));
        label_4->setStyleSheet(QStringLiteral("font: 16pt \"Times New Roman\";"));
        label_4->setAlignment(Qt::AlignCenter);
        pushButton_5 = new QPushButton(fourthDialog);
        pushButton_5->setObjectName(QStringLiteral("pushButton_5"));
        pushButton_5->setGeometry(QRect(430, 370, 75, 23));
        label = new QLabel(fourthDialog);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(0, 0, 681, 111));
        label->setPixmap(QPixmap(QString::fromUtf8("../imagens/logo.png")));
        pushButton_2 = new QPushButton(fourthDialog);
        pushButton_2->setObjectName(QStringLiteral("pushButton_2"));
        pushButton_2->setGeometry(QRect(130, 290, 51, 41));
        lcdNumber_2 = new QLCDNumber(fourthDialog);
        lcdNumber_2->setObjectName(QStringLiteral("lcdNumber_2"));
        lcdNumber_2->setGeometry(QRect(350, 260, 71, 51));
        pushButton_3 = new QPushButton(fourthDialog);
        pushButton_3->setObjectName(QStringLiteral("pushButton_3"));
        pushButton_3->setGeometry(QRect(460, 230, 51, 41));
        pushButton_4 = new QPushButton(fourthDialog);
        pushButton_4->setObjectName(QStringLiteral("pushButton_4"));
        pushButton_4->setGeometry(QRect(460, 280, 51, 41));
        label_11 = new QLabel(fourthDialog);
        label_11->setObjectName(QStringLiteral("label_11"));
        label_11->setGeometry(QRect(90, 290, 31, 16));
        label_11->setStyleSheet(QStringLiteral("font: 75 12pt \"Times New Roman\";"));
        label_12 = new QLabel(fourthDialog);
        label_12->setObjectName(QStringLiteral("label_12"));
        label_12->setGeometry(QRect(430, 290, 21, 16));
        label_12->setStyleSheet(QStringLiteral("font: 75 12pt \"Times New Roman\";"));

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
