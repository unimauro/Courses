using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class KillBall : MonoBehaviour
{
	private void OnMouseDown()
	{
		Destroy(gameObject);
	}

}
