using System.Net;
using System.Net.Sockets;
using System.Text;

namespace Objektno_programirenje_LV5___Kuna
{
    public partial class Form1 : Form
    {
        Random rnd = new Random();
        List<string> colorList = new List<string> { "red", "green", "blue", "yellow", "purple" };
        String color = "red";
        String listItem = " ";
        String sendString = " ";
        TcpClient client = new TcpClient();
        NetworkStream stream;

        byte[] prepareForTransmission(string data)
        {
            int byteCount = Encoding.ASCII.GetByteCount(data);
            byte[] sendData = new byte[byteCount];
            sendData = Encoding.ASCII.GetBytes(data);
            return sendData;
        }

        void colorPicker()
        {
            if (rnd.Next(colorList.Count) == 0) color = "red";
            else if (rnd.Next(colorList.Count) == 1) color = "green";
            else if (rnd.Next(colorList.Count) == 2) color = "blue";
            else if (rnd.Next(colorList.Count) == 3) color = "yellow";
            else color = "purple";
        }


        public Form1()
        {
            InitializeComponent();
        }

        private void buttonRandomtab2_Click(object sender, EventArgs e)
        {
            textBoxXTocka1tab2.Text = rnd.Next(0,800).ToString();
            textBoxYTocka1tab2.Text = rnd.Next(0,600).ToString();
            textBoxXTocka2tab2.Text = rnd.Next(0,800).ToString();
            textBoxYTocka2tab2.Text = rnd.Next(0,600).ToString();
            colorPicker();
            textBoxBojatab2.Text = color;
        }

        private void buttonRandomtab3_Click(object sender, EventArgs e)
        {
            textBoxXTocka1tab3.Text = rnd.Next(0, 800).ToString();
            textBoxYTocka1tab3.Text = rnd.Next(0, 600).ToString();
            textBoxXTocka2tab3.Text = rnd.Next(0, 800).ToString();
            textBoxYTocka2tab3.Text = rnd.Next(0, 600).ToString();
            textBoxXTocka3tab3.Text = rnd.Next(0, 800).ToString();
            textBoxYTocka3tab3.Text = rnd.Next(0, 600).ToString();
            colorPicker();
            textBoxBojatab3.Text = color;
        }

        private void buttonRandomtab4_Click(object sender, EventArgs e)
        {
            textBoxXTocka1tab4.Text = rnd.Next(0, 800).ToString();
            textBoxYTocka1tab4.Text = rnd.Next(0, 600).ToString();
            textBoxXTocka2tab4.Text = rnd.Next(0, 500).ToString();//height
            textBoxYTocka2tab4.Text = rnd.Next(0, 500).ToString();//width
            colorPicker();
            textBoxBojatab4.Text = color;
        }

        private void buttonRandomtab5_Click(object sender, EventArgs e)
        {
            textBoxXTockatab5.Text = rnd.Next(0, 800).ToString();
            textBoxYTockatab5.Text = rnd.Next(0, 600).ToString();
            colorPicker();
            textBoxBojatab5.Text = color;
        }

        private void buttonRandomtab6_Click(object sender, EventArgs e)
        {
            textBoxXCentartab6.Text = rnd.Next(0, 800).ToString();
            textBoxYCentartab6.Text = rnd.Next(0, 600).ToString();
            textBoxRadiustab6.Text = rnd.Next(0, 100).ToString();
            colorPicker();
            textBoxBojatab6.Text = color;
        }

        private void buttonRandomtab7_Click(object sender, EventArgs e)
        {
            textBoxXCentartab7.Text = rnd.Next(0, 800).ToString();
            textBoxYCentartab7.Text = rnd.Next(0, 600).ToString();
            textBoxRadius1tab7.Text = rnd.Next(0, 100).ToString();
            textBoxRadius2tab7.Text = rnd.Next(0, 100).ToString();
            colorPicker();
            textBoxBojatab7.Text = color;
        }

        private void buttonAddPoint_Click(object sender, EventArgs e)
        {
            listItem = textBoxXTockatab5.Text + " " + textBoxYTockatab5.Text;
            listBoxPolygon.Items.Add(listItem);
        }

        private void buttonResettab5_Click(object sender, EventArgs e)
        {
            listBoxPolygon.Items.Clear();
        }

        private void buttonConnect_Click(object sender, EventArgs e)
        {
            panelConnection.BackColor = Color.Green;
            client = new TcpClient(textBoxHostName.Text, int.Parse(textBoxHostPort.Text));
        }

        private void buttonCloseConnection_Click(object sender, EventArgs e)
        {
            panelConnection.BackColor = Color.Red;
            client.Close();
        }

        private void buttonSendtab2_Click(object sender, EventArgs e)
        {
            sendString = "Line " + textBoxBojatab2.Text + " " + textBoxXTocka1tab2.Text + " " + textBoxYTocka1tab2.Text + " " +
                textBoxXTocka2tab2.Text + " " + textBoxYTocka2tab2.Text;
            stream = client.GetStream();
            stream.Write(prepareForTransmission(sendString), 0, prepareForTransmission(sendString).Length);
            
        }

        private void buttonSendtab3_Click(object sender, EventArgs e)
        {
            sendString = "Triangle " + textBoxBojatab3.Text + " " + textBoxXTocka1tab3.Text + " " + textBoxYTocka1tab3.Text
                + " " + textBoxXTocka2tab3.Text + " " + textBoxYTocka2tab3.Text + " " + textBoxXTocka3tab3.Text + " "
                + textBoxYTocka3tab3.Text;
                stream = client.GetStream();
            stream.Write(prepareForTransmission(sendString), 0, prepareForTransmission(sendString).Length);
        }

        private void buttonSendtab4_Click(object sender, EventArgs e)
        {
            sendString = "Rectangle " + textBoxBojatab4.Text + " " + textBoxXTocka1tab4.Text + " " + textBoxYTocka1tab4.Text
                + " " + textBoxXTocka2tab4.Text + " " + textBoxYTocka2tab4.Text;
            stream = client.GetStream();
            stream.Write(prepareForTransmission(sendString), 0, prepareForTransmission(sendString).Length);
            
        }

        private void buttonSendtab5_Click(object sender, EventArgs e)
        {
            String listString = "";
            for (int i = 0; i < listBoxPolygon.Items.Count; i++) {
                listString += listBoxPolygon.Items[i].ToString() + " ";
            }
            sendString = "Polygon " + textBoxBojatab5.Text + " " + listString;
            stream = client.GetStream();
            stream.Write(prepareForTransmission(sendString), 0, prepareForTransmission(sendString).Length);
            
        }

        private void buttonSendtab6_Click(object sender, EventArgs e)
        {
            sendString = "Circle " + textBoxBojatab6.Text + " " + textBoxXCentartab6.Text + " " + textBoxYCentartab6.Text
                + " " + textBoxRadiustab6.Text;
            stream = client.GetStream();
            stream.Write(prepareForTransmission(sendString), 0, prepareForTransmission(sendString).Length);
            
        }

        private void buttonSendtab7_Click(object sender, EventArgs e)
        {
            sendString = "Ellipse " + textBoxBojatab7.Text + " " + textBoxXCentartab7.Text + " " + textBoxYCentartab7.Text
                + " " + textBoxRadius1tab7.Text + " " + textBoxRadius2tab7.Text;
            stream = client.GetStream();
            stream.Write(prepareForTransmission(sendString), 0, prepareForTransmission(sendString).Length);
            
        }
    }
}