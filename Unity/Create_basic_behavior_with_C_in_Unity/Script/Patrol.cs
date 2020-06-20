using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Patrol : MonoBehaviour
{
	[Tooltip ("Unidade de Distancia")]
	//[Range (10,40)]
	public int distance;
	[Tooltip ("Velocidad del objeto")]
	//[Min (4)]
	public float speed;
	private Vector3 startPos, endPos, targetPos;

	private void Awake()
	{
		startPos = transform.position;
		endPos = startPos
           + transform.forward
           * distance;
	}

	void Update()
	{
		if (Vector3.Distance(transform.position, startPos)<=0.1)
		{
			targetPos=endPos;
		}
		if (Vector3.Distance(transform.position,endPos)<=0.1)
		{
			targetPos=startPos;
		}
		transform.position = Vector3.MoveTowards (transform.position, 
		targetPos, speed * Time.deltaTime);
	}



}
