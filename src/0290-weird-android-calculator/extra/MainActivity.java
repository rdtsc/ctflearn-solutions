package p004de.vidar.weirdcalculator;

import android.os.Bundle;
import android.support.p003v7.app.AppCompatActivity;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

/* renamed from: de.vidar.weirdcalculator.MainActivity */
public class MainActivity extends AppCompatActivity {
    private View view;

    /* access modifiers changed from: protected */
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView((int) C0266R.layout.activity_main);
        this.view = findViewById(C0266R.C0268id.txtExpression);
    }

    public void createBackground(View v) {
        String s = ((EditText) this.view).getText().toString();
        try {
            TextView result = (TextView) findViewById(C0266R.C0268id.lblResult);
            result.setText("");
            result.setText(String.valueOf(Parser.eval(s)));
        } catch (Exception e) {
            Toast.makeText(this, e.getMessage(), 1).show();
        }
    }
}
