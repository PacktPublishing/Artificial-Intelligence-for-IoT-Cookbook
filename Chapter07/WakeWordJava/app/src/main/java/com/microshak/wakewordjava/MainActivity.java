package com.microshak.wakewordjava;

import androidx.appcompat.app.AppCompatActivity;
import com.microsoft.cognitiveservices.speech.KeywordRecognitionModel;
import com.microsoft.cognitiveservices.speech.SpeechConfig;
import com.microsoft.cognitiveservices.speech.SpeechRecognizer;
import com.microsoft.cognitiveservices.speech.audio.AudioConfig;

import java.io.IOException;
import java.util.ArrayList;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Future;

import android.content.res.AssetManager;
import android.os.Bundle;
import android.text.Layout;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private static String SpeechSubscriptionKey = "<Your subcription key here>";
    private static String SpeechRegion = "westus2";

    private TextView recognizedTextView;
    private static String LanguageRecognition = "en-US";
    private Button recognizeKwsButton;


    private static String Keyword = "computer";
    private static String KeywordModel = "computer.zip";// set your own keyword package name.

    private static String DeviceGeometry = "Linear4";
    private static String SelectedGeometry = "Linear4";

    final AssetManager assets = this.getAssets();

    private void setTextbox(final String s) {
        MainActivity.this.runOnUiThread(() -> {
            recognizedTextView.setText(s);

            final Layout layout = recognizedTextView.getLayout();
            if (layout != null) {
                int scrollDelta = layout.getLineBottom(recognizedTextView.getLineCount() - 1)
                        - recognizedTextView.getScrollY() - recognizedTextView.getHeight();
                if (scrollDelta > 0) {
                    recognizedTextView.scrollBy(0, scrollDelta);
                }
            }
        });
    }

    private AudioConfig getAudioConfig() {
        return AudioConfig.fromDefaultMicrophoneInput();
    }

    private interface OnTaskCompletedListener<T> {
        void onCompleted(T taskResult);
    }

    protected static ExecutorService s_executorService;

    public static SpeechConfig getSpeechConfig() {
        SpeechConfig speechConfig = SpeechConfig.fromSubscription(SpeechSubscriptionKey, SpeechRegion);

        // PMA parameters
        speechConfig.setProperty("DeviceGeometry", DeviceGeometry);
        speechConfig.setProperty("SelectedGeometry", SelectedGeometry);
        speechConfig.setSpeechRecognitionLanguage(LanguageRecognition);

        return speechConfig;
    }

    private <T> void setOnTaskCompletedListener(Future<T> task, OnTaskCompletedListener<T> listener) {
        s_executorService.submit(() -> {
            T result = task.get();
            listener.onCompleted(result);
            return null;
        });
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        recognizeKwsButton = findViewById(R.id.buttonRecognizeKws);
        recognizedTextView = findViewById(R.id.recognizedText);

        recognizeKwsButton.setOnClickListener(new View.OnClickListener() {
            private static final String delimiter = "\n";
            private final ArrayList<String> content = new ArrayList<>();
            private SpeechRecognizer reco = null;

            @Override
            public void onClick(View view) {
                content.clear();
                content.add("");
                content.add("");
                try {
                    final KeywordRecognitionModel keywordRecognitionModel = KeywordRecognitionModel.fromStream(assets.open(KeywordModel), Keyword, true);

                    final Future<Void> task = reco.startKeywordRecognitionAsync(keywordRecognitionModel);
                    setOnTaskCompletedListener(task, result -> {
                        content.set(0, "say `" + Keyword + "`...");
                        setTextbox(TextUtils.join(delimiter, content));
                    });

                } catch (IOException e) {
                    e.printStackTrace();
                }
            }});
    }
}
