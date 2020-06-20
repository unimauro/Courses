using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Spin : MonoBehaviour
{
    // Start is called before the first frame update

    public float spinSpeed; 

    // Update is called once per frame
    void Update()
    {
        transform.Rotate (Vector3.up, spinSpeed*Time.deltaTime);
    }
}
