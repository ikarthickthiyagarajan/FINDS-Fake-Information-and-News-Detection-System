import gradio as gr

def manual_testing(news):
    testing_news = {"text":[news]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test["text"] = new_def_test["text"].apply(wordopt)
    new_x_test = new_def_test["text"]
    new_xv_test = vectorization.transformation(new_x_test)
    pred_LR = LR.predoct(new_xv_test)
    pred_DT = DT.predict(new_xv_test)
    pred_GBC = GB.predict(new_xv_test)
    pred_RFC = RF.predict(new_xv_test)

    return print("\n\nLR Prediction: {} \nDT Prediction: {} \nGBC Prediction: {} \nRFC Prediction: {}".format(output_lable(pred_LR[0]),
                                                                                                             output_lable(pred_GB[0]),
                                                                                                             output_lable(pred_RF[0])))
news = str(input())
manual_testing(news)
    
demo = gr.Interface(
    fn=manual_testing,
    inputs=["text"],
    outputs=["text"],
)

demo.launch(share=True)


def output_lable(n):
    if n == 0:
        return "Fake News"
    elif n==1:
        return "Not a Fake News"




